import os
import requests
from datetime import datetime, UTC

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
    """
    Example:

    ███████░░░░░░░░░░░░
    """

    percentage = min(current / goal, 1)

    filled = int(width * percentage)

    return "█" * filled + "░" * (width - filled)


# -----------------------------
# Markdown Generator
# -----------------------------

def generate_markdown(stats):

    percentage = (stats["total"] / GOAL) * 100

markdown = f"""
| Difficulty | Solved |
|------------|-------:|
| 🟢 Easy | {stats['easy']} |
| 🟡 Medium | {stats['medium']} |
| 🔴 Hard | {stats['hard']} |
| ⭐ **Total** | **{stats['total']}** |

---

## 🎯 Progress

<progress value="{stats['total']}" max="{GOAL}"></progress>

**{stats['total']} / {GOAL} Problems ({percentage:.1f}%)**

---

## 🌍 Global Ranking

**{stats['ranking']:,}**

---

_Last Updated: {datetime.now(UTC).strftime("%d %b %Y %H:%M UTC")}_
"""

    return markdown
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

    markdown = generate_markdown(stats)

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
