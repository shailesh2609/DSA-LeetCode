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
    """
    Generate the difficulty breakdown section.
    """

    values = {
        "Easy": stats["easy"],
        "Medium": stats["medium"],
        "Hard": stats["hard"],
    }

    max_value = max(values.values()) if values else 1

    icons = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
    }

    lines = [
        "## 📈 Difficulty Breakdown",
        "",
        "```text",
    ]

    for difficulty in ("Easy", "Medium", "Hard"):

        solved = values[difficulty]

        filled = (
            max(1, int(solved / max_value * TOPIC_BAR_LENGTH))
            if solved > 0
            else 0
        )

        bar = "█" * filled

        lines.append(
            f"{icons[difficulty]} "
            f"{difficulty:<10}"
            f"{bar:<20}"
            f"{solved:>4}"
        )

        lines.append("")

    return "\n".join(lines)


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
    Generate the Recently Solved section.
    """

    problems = sorted(
        problems,
        key=lambda p: get_last_commit_timestamp(p.folder),
        reverse=True,
    )

    icons = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
    }

    lines = [
        "## 🔥 Recently Solved",
        "",
    ]

    for problem in problems[:limit]:

        icon = icons.get(
            problem.difficulty,
            "⚪",
        )

        url = (
            f"https://leetcode.com/problems/"
            f"{problem.slug}/"
        )

        lines.append(
            f"{icon} {problem.frontend_id}. "
            f"[{problem.title}]({url})"
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
    Shows Top 10 topics and keeps the complete list
    inside a collapsible details block.
    """

    counter = topic_distribution(problems)

    if not counter:
        return "## 📚 Top Topics\n\n_No data available._"

    total = len(problems)
    max_count = max(counter.values())

    sorted_topics = sorted(
        counter.items(),
        key=lambda item: (-item[1], item[0]),
    )

    max_topic_length = max(
        len(topic)
        for topic, _ in sorted_topics
    )

    def build_table(topics):

        lines = ["```text"]

        for topic, count in topics:

            percentage = count / total * 100

            filled = max(
                1,
                int(count / max_count * TOPIC_BAR_LENGTH),
            )

            bar = "█" * filled

            lines.append(
                f"{topic:<{max_topic_length}} "
                f"{bar:<{TOPIC_BAR_LENGTH}} "
                f"{count:>3} "
                f"({percentage:4.1f}%)"
            )

        lines.append("```")

        return "\n".join(lines)

    top_topics = sorted_topics[:10]

    remaining_topics = sorted_topics[10:]

    markdown = [
        "## 📚 Top Topics",
        "",
        build_table(top_topics),
    ]

    if remaining_topics:

        markdown.extend([
            "",
            "<details>",
            "<summary><b>Show Complete Topic Distribution</b></summary>",
            "",
            build_table(remaining_topics),
            "",
            "</details>",
        ])

    return "\n".join(markdown)


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
