from collections import Counter
from datetime import datetime, UTC

from config import GOAL
from repository import get_last_commit_timestamp


# ==========================================================
# Constants
# ==========================================================

START_MARKER = "<!-- LEETCODE_STATS_START -->"
END_MARKER = "<!-- LEETCODE_STATS_END -->"

BAR_LENGTH = 20
TOPIC_BAR_LENGTH = 15


# ==========================================================
# Statistics
# ==========================================================

def parse_stats(user_data):
    """
    Parse LeetCode GraphQL response.
    """

    stats = {
        "easy": 0,
        "medium": 0,
        "hard": 0,
        "total": 0,
        "ranking": 0,
    }

    for item in user_data["submitStats"]["acSubmissionNum"]:

        difficulty = item["difficulty"]

        count = item["count"]

        if difficulty == "Easy":
            stats["easy"] = count

        elif difficulty == "Medium":
            stats["medium"] = count

        elif difficulty == "Hard":
            stats["hard"] = count

        elif difficulty == "All":
            stats["total"] = count

    stats["ranking"] = user_data["profile"]["ranking"]

    return stats


# ==========================================================
# Progress Bar
# ==========================================================

def progress_bar(current, goal, width=BAR_LENGTH):
    """
    Generate a unicode progress bar.
    """

    filled = min(
        width,
        int(current / goal * width),
    )

    empty = width - filled

    return "█" * filled + "░" * empty


# ==========================================================
# Badge
# ==========================================================

def build_leetcode_badge(stats):

    solved = stats["total"]

    return (
        '<p align="center">\n'
        f'<img src="https://img.shields.io/badge/'
        f'LeetCode-{solved}%20Solved-FFA116'
        f'?style=for-the-badge'
        f'&logo=leetcode'
        f'&logoColor=white"/>\n'
        '</p>'
    )


# ==========================================================
# Sections
# ==========================================================

def build_difficulty(stats):

    return f"""
## 📈 Difficulty Breakdown

🟢 Easy&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{stats["easy"]}

🟡 Medium&nbsp;&nbsp;{stats["medium"]}

🔴 Hard&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{stats["hard"]}
"""


def build_progress(stats):

    percentage = stats["total"] / GOAL * 100

    bar = progress_bar(
        stats["total"],
        GOAL,
    )

    return f"""
## 🎯 Progress

{bar}

**{stats["total"]} / {GOAL} Problems**

📈 **Completion:** {percentage:.1f}%
"""


def build_ranking(stats):

    return f"""
## 🌍 Global Rank

🏅 **{stats["ranking"]:,}**
"""


# ==========================================================
# Recently Solved
# ==========================================================

def recently_solved(problems, limit=5):
    """
    Generate the 'Recently Solved' section.
    """

    problems = sorted(
        problems,
        key=lambda p: get_last_commit_timestamp(p.folder),
        reverse=True,
    )

    lines = [
        "## 🔥 Recently Solved",
        "",
    ]

    icons = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
    }

    for problem in problems[:limit]:

        icon = icons.get(
            problem.difficulty,
            "⚪",
        )

        lines.append(
            f"{icon} {problem.frontend_id}. {problem.title}"
        )

        lines.append("")

    return "\n".join(lines)


# ==========================================================
# Topic Distribution
# ==========================================================

def topic_distribution(problems):
    """
    Count occurrences of every topic.
    """

    counter = Counter()

    for problem in problems:

        for topic in problem.topics:

            counter[topic] += 1

    return counter


# ==========================================================
# Problem Distribution
# ==========================================================

def problem_distribution(problems):
    """
    Generate the topic distribution section.
    """

    counter = topic_distribution(problems)

    if not counter:
        return "## 📚 Topic Distribution\n\n_No data available._"

    total = len(problems)

    max_count = max(counter.values())

    max_topic = max(
        len(topic)
        for topic in counter
    )

    lines = [
        "## 📚 Top Topics",
        "",
        "```text",
    ]

    for topic, count in sorted(
        counter.items(),
        key=lambda item: (-item[1], item[0]),
    ):

        percentage = count / total * 100

        filled = max(
            1,
            int(
                count / max_count * TOPIC_BAR_LENGTH
            ),
        )

        bar = "█" * filled

        lines.append(
            f"{topic:<{max_topic}} "
            f"{bar:<{TOPIC_BAR_LENGTH}} "
            f"{count:>3} "
            f"({percentage:4.1f}%)"
        )

    lines.append("```")

    return "\n".join(lines)


# ==========================================================
# Footer
# ==========================================================

def build_footer():
    """
    Generate footer.
    """

    return (
        "🕒 **Last Updated**\n\n"
        + datetime.now(UTC).strftime("%d %b %Y • %H:%M UTC")
    )


# ==========================================================
# Markdown Generator
# ==========================================================

def generate_markdown(stats, problems):
    """
    Generate the complete markdown section for README.
    """

    sections = [
        build_leetcode_badge(stats),
        build_difficulty(stats),
        build_progress(stats),
        build_ranking(stats),
        problem_distribution(problems),
        recently_solved(problems),
        build_footer(),
    ]

    return "\n\n---\n\n".join(sections)


# ==========================================================
# README Updater
# ==========================================================

def update_readme(markdown):
    """
    Replace everything between the README markers.
    """

    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        raise RuntimeError(
            "README markers not found."
        )

    start += len(START_MARKER)

    updated = (
        content[:start]
        + "\n\n"
        + markdown
        + "\n\n"
        + content[end:]
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated)
