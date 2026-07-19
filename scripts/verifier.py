from graphql import fetch_problem_metadata
from models import Problem
from repository import get_problem_folders
from utils import (
    extract_problem_id,
    folder_to_slug,
    rename_problem_folder,
)


def verify_problem_folders():
    """
    Verify every LeetCode problem folder.

    - Renames folders if LeetSync generated an incorrect ID.
    - Returns a list of verified Problem objects.
    """

    print("\nVerifying problem folders...\n")

    problems = []

    for folder in get_problem_folders():

        slug = folder_to_slug(folder)
        folder_id = extract_problem_id(folder)

        metadata = fetch_problem_metadata(slug)

        if metadata is None:
            print(f"Skipping '{folder}' (metadata not found).")
            continue

        frontend_id = metadata["questionFrontendId"]
        title = metadata["title"]
        difficulty = metadata["difficulty"]

        topics = [
            tag["name"]
            for tag in metadata["topicTags"]
        ]

        if folder_id != frontend_id:

            correct_folder = f"{frontend_id}-{slug}"

            print(
                f"Renamed: {folder} -> {correct_folder}"
            )

            rename_problem_folder(
                folder,
                correct_folder,
            )

            folder = correct_folder

        problems.append(
            Problem(
                frontend_id=frontend_id,
                title=title,
                difficulty=difficulty,
                topics=topics,
                folder=folder,
                slug=slug,
            )
        )

    print(f"\nVerified {len(problems)} problems.\n")

    return problems
