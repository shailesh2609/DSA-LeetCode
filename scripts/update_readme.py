import os
import json
import requests
from datetime import datetime, UTC

from utils import (
    get_problem_folders,
    extract_problem_id,
    folder_to_slug,
    get_last_commit_timestamp,
    problem_title,
)

CACHE_DIR = ".cache"
CACHE_FILE = os.path.join(CACHE_DIR, "topics.json")

# -----------------------------
# Configuration
# -----------------------------

USERNAME = os.getenv("LEETCODE_USERNAME")
GOAL = 500

GRAPHQL_URL = "https://leetcode.com/graphql"

# -----------------------------
# GraphQL Query
# -----------------------------

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {

    profile {
      ranking
    }

    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    difficulty

    topicTags {
      name
    }
  }
}
"""

def load_cache():
    """
    Load cached LeetCode metadata.
    """

    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache):
    os.makedirs(CACHE_DIR, exist_ok=True)

    print("Saving cache:")
    print(json.dumps(cache, indent=2))

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

# -----------------------------
# Request Function
# -----------------------------

def fetch_leetcode_stats(username: str):
    """
    Fetch statistics from LeetCode GraphQL API.
    """

    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": QUERY,
            "variables": {
                "username": username
            }
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    return data["data"]["matchedUser"]

def fetch_problem_metadata(slug):
    """
    Fetch metadata for a single problem.
    """

    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": QUESTION_QUERY,
            "variables": {
                "titleSlug": slug
            }
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    return data["data"]["question"]

def update_topic_cache():

    cache = load_cache()

    folders = get_problem_folders()

    updated = False

    for folder in folders:

        print(f"Processing: {folder}")

        pid = extract_problem_id(folder)

        if pid in cache:
            print(f"Already cached: {pid}")
            continue

        print(f"Fetching metadata for {folder}")

        metadata = fetch_problem_metadata(
            folder_to_slug(folder)
        )

        cache[pid] = {
            "title": metadata["title"],
            "difficulty": metadata["difficulty"],
            "topics": [
                tag["name"]
                for tag in metadata["topicTags"]
            ]
        }

        updated = True

    if updated:
        save_cache(cache)
        print("Cache saved.")

    return cache

# -----------------------------
# Parse Response
# -----------------------------

def parse_stats(user_data):
    """
    Convert GraphQL response into
    an easy-to-use dictionary.
    """

    stats = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0,
        "All": 0
    }

    submissions = user_data["submitStats"]["acSubmissionNum"]

    for item in submissions:
        difficulty = item["difficulty"]
        count = item["count"]

        stats[difficulty] = count

    ranking = user_data["profile"]["ranking"]

    return {
        "easy": stats["Easy"],
        "medium": stats["Medium"],
        "hard": stats["Hard"],
        "total": stats["All"],
        "ranking": ranking,
    }


# -----------------------------
# Progress Bar
# -----------------------------

def progress_bar(current, goal, width=20):
    filled = int((current / goal) * width)
    return "🟩" * filled + "⬜" * (width - filled)
  
# -----------------------------
# Markdown Generator
# -----------------------------

def generate_markdown(stats, cache):

    percentage = stats["total"] / GOAL * 100

    bar = progress_bar(stats["total"], GOAL)

    markdown = f"""
| Difficulty | Solved |
|------------|-------:|
| 🟢 Easy | {stats['easy']} |
| 🟡 Medium | {stats['medium']} |
| 🔴 Hard | {stats['hard']} |
| ⭐ **Total** | **{stats['total']}** |

---

### 🎯 Progress

{bar}

**{stats['total']} / {GOAL} Problems ({percentage:.1f}%)**

---

## 🌍 Global Ranking

**{stats['ranking']:,}**

---

{problem_distribution(cache)}

---

{recently_solved(cache)}

---

_Last Updated: {datetime.now(UTC).strftime("%d %b %Y %H:%M UTC")}_
"""

    return markdown


def recently_solved(cache, limit=5):

    folders = get_problem_folders()

    folders.sort(
        key=get_last_commit_timestamp,
        reverse=True
    )

    lines = [
        "## 🔥 Recently Solved",
        ""
    ]

    for folder in folders[:limit]:

        pid = extract_problem_id(folder)

        data = cache.get(pid)

        if not data:
            continue

        difficulty = data["difficulty"]

        icon = {
            "Easy": "🟢",
            "Medium": "🟡",
            "Hard": "🔴"
        }.get(difficulty, "⚪")

        lines.append(f"{icon} {data['title']}")

    return "\n".join(lines)
    
from collections import Counter

def problem_distribution(cache):
    """
    Generates a nicely formatted topic distribution.
    """

    counter = Counter()

    for problem in cache.values():
        for topic in problem["topics"]:
            counter[topic] += 1

    if not counter:
        return "## 📚 Problem Distribution\n\nNo data yet."

    max_count = max(counter.values())

    lines = [
        "## 📚 Problem Distribution",
        ""
    ]

    for topic, count in counter.most_common(10):

        bar = "█" * int((count / max_count) * 15)

        lines.append(
            f"{topic:<22} {bar:<15} {count}"
        )

    return "\n".join(lines)
    
def topic_distribution(cache):
    """
    Count how many problems belong to each topic.
    """

    counter = Counter()

    for problem in cache.values():

        for topic in problem["topics"]:

            counter[topic] += 1

    return counter

  
# -----------------------------
# README Updater
# -----------------------------

START_MARKER = "<!-- LEETCODE_STATS_START -->"
END_MARKER = "<!-- LEETCODE_STATS_END -->"


def update_readme(markdown):
    """
    Replace everything between the markers
    in README.md with freshly generated markdown.
    """

    readme_path = "README.md"

    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        raise Exception(
            "README markers not found.\n"
            "Please add:\n"
            "<!-- LEETCODE_STATS_START -->\n"
            "<!-- LEETCODE_STATS_END -->"
        )

    start += len(START_MARKER)

    new_content = (
        content[:start]
        + "\n\n"
        + markdown
        + "\n"
        + content[end:]
    )

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_content)


# -----------------------------
# Main
# -----------------------------

def main():

    if not USERNAME:
        raise Exception(
            "Repository Variable LEETCODE_USERNAME not found."
        )

    print(f"Fetching LeetCode stats for {USERNAME}...")

    user = fetch_leetcode_stats(USERNAME)

    stats = parse_stats(user)
    
    cache = update_topic_cache()

    markdown = generate_markdown(stats, cache)

    update_readme(markdown)

    print("README updated successfully.")


# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print("ERROR:")
        print(e)
        raise
