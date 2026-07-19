from datetime import datetime, UTC
from collections import Counter

from repository import get_last_commit_timestamp

# -----------------------------
# Parse Response
# -----------------------------

from config import GOAL

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
    

def build_stats_table(stats):

    return f"""
| Difficulty | Solved |
|------------|-------:|
| 🟢 Easy | {stats['easy']} |
| 🟡 Medium | {stats['medium']} |
| 🔴 Hard | {stats['hard']} |
| ⭐ **Total** | **{stats['total']}** |
"""

def build_progress(stats):

    percentage = stats["total"] / GOAL * 100

    bar = progress_bar(
        stats["total"],
        GOAL,
    )

    return f"""
### 🎯 Progress

{bar}

**{stats['total']} / {GOAL} Problems ({percentage:.1f}%)**
"""

def build_ranking(stats):

    return f"""
## 🌍 Global Ranking

**{stats['ranking']:,}**
"""

def build_footer():

    return (
        "_Last Updated: "
        + datetime.now(UTC).strftime("%d %b %Y %H:%M UTC")
        + "_"
    )
    
    
# -----------------------------
# Markdown Generator
# -----------------------------

def generate_markdown(stats, problems):

    return f"""
{build_stats_table(stats)}

---

{build_progress(stats)}

---

{build_ranking(stats)}

---

{problem_distribution(problems)}

---

{recently_solved(problems)}

---

{build_footer()}
"""


def recently_solved(problems, limit=5):

    problems = sorted(
        problems,
        key=lambda p: get_last_commit_timestamp(p.folder),
        reverse=True,
    )

    lines = [
        "## 🔥 Recently Solved",
        ""
    ]

    for problem in problems[:limit]:

        difficulty = problem.difficulty

        icon = {
            "Easy": "🟢",
            "Medium": "🟡",
            "Hard": "🔴"
        }.get(difficulty, "⚪")

        lines.append(f"{icon} {problem.title}<br>")

    return "\n".join(lines)
    
from collections import Counter

def problem_distribution(problems):

    counter = topic_distribution(problems)

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
    
def topic_distribution(problems):
    """
    Count how many problems belong to each topic.
    """

    counter = Counter()

    for problem in problems:

        for topic in problem.topics:

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
