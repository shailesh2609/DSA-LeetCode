import os
from cache import (
    load_cache,
    save_cache,
)
from graphql import (
    fetch_leetcode_stats,
    fetch_problem_metadata,
)
from verifier import verify_problem_folders
from datetime import datetime, UTC

from utils import (
    get_problem_folders,
    extract_problem_id,
    folder_to_slug,
    get_last_commit_timestamp,
    problem_title,
    problem_number,
    rename_problem_folder,
)


# -----------------------------
# Configuration
# -----------------------------

USERNAME = os.getenv("LEETCODE_USERNAME")
GOAL = 500


# -----------------------------
# Request Function
# -----------------------------


def update_topic_cache():

    cache = load_cache()

    folders = get_problem_folders()

    updated = False

    for folder in sorted(folders, key=problem_number):

        print(f"Processing: {folder}")

        print(f"Fetching metadata for {folder}")

        metadata = fetch_problem_metadata(
            folder_to_slug(folder)
        )

        if metadata is None:
            print(f"Skipping {folder}: metadata not found.")
            continue

        official_id = metadata["questionFrontendId"]

        # Always use the official LeetCode ID as the cache key
        cache[official_id] = {
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

        lines.append(f"{icon} {data['title']}<br>")

    return "\n".join(lines)
    
from collections import Counter

def problem_distribution(cache):

    counter = topic_distribution(cache)

    if not counter:
        return "## 📚 Problem Distribution\n\n_No data available._"

    max_count = max(counter.values())
    BAR_LENGTH = 15

    lines = [
        "## 📚 Problem Distribution",
        "",
        "```text"
    ]

    max_topic_length = max(len(topic) for topic in counter.keys())

    for topic, count in sorted(counter.items(), key=lambda x: (-x[1], x[0])):

        filled = max(1, int(count / max_count * BAR_LENGTH))

        bar = "█" * filled

        lines.append(
            f"{topic:<{max_topic_length}}   {bar:<15} {count}"
        )

    # Close the code block
    lines.append("```")

    # Return AFTER processing all topics
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

    verify_problem_folders()

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
