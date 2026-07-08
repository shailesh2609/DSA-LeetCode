import os
import requests
from datetime import datetime

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

    bar = progress_bar(stats["total"], GOAL)

    markdown = f"""
| Difficulty | Solved |
|------------|-------:|
| 🟢 Easy | {stats['easy']} |
| 🟡 Medium | {stats['medium']} |
| 🔴 Hard | {stats['hard']} |
| ⭐ **Total** | **{stats['total']}** |

### 🎯 Progress

{bar}

**{stats['total']} / {GOAL} Problems**

### 🌍 Global Ranking

{stats['ranking']}

_Last Updated: {datetime.utcnow().strftime("%d %b %Y %H:%M UTC")}_
"""

    return markdown
