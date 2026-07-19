import os
from graphql import (
    fetch_leetcode_stats,
)
from verifier import verify_problem_folders
from datetime import datetime, UTC

from utils import (
    get_problem_folders,
    get_last_commit_timestamp,
    problem_title,
)


# -----------------------------
# Configuration
# -----------------------------

USERNAME = os.getenv("LEETCODE_USERNAME")
GOAL = 500




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

    verified_problems = verify_problem_folders()

    markdown = generate_markdown(
        stats,
        verified_problems,
    )

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
