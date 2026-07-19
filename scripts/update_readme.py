from config import USERNAME

from graphql import fetch_leetcode_stats
from verifier import verify_problem_folders

from markdown import (
    parse_stats,
    generate_markdown,
    update_readme,
)

# -----------------------------
# Main
# -----------------------------

def main():

    if not USERNAME:
        raise RuntimeError(
            "Repository Variable LEETCODE_USERNAME not found."
        )

    print(f"Fetching LeetCode stats for '{USERNAME}'...")

    user = fetch_leetcode_stats(USERNAME)

    stats = parse_stats(user)

    print("Verifying repository...")

    problems = verify_problem_folders()

    print(f"Verified {len(problems)} problems.")

    markdown = generate_markdown(
        stats,
        problems,
    )

    print("Updating README...")

    update_readme(markdown)

    print("Done ✅")


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
