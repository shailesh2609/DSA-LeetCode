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
    Verify every problem folder and return the verified metadata.
    """

    print("\nVerifying problem folders...\n")

    verified_problems = []

    for folder in get_problem_folders():

        slug = folder_to_slug(folder)

        metadata = fetch_problem_metadata(slug)

        if metadata is None:
            print(f"Skipping {folder}")
            continue

        official_id = metadata["questionFrontendId"]

        if extract_problem_id(folder) != official_id:

            correct_folder = (
                f"{official_id}-{slug}"
            )

            print(f"Renaming:")
            print(f"  {folder}")
            print(f"  → {correct_folder}\n")

            rename_problem_folder(
                folder,
                correct_folder,
            )

            folder = correct_folder

        verified_problems.append(
            Problem(
                frontend_id=official_id,
                title=metadata["title"],
                difficulty=metadata["difficulty"],
                topics=[
                    tag["name"]
                    for tag in metadata["topicTags"]
                ],
                folder=folder,
                slug=slug,
            )
        )

    print("Folder verification complete.\n")

    return verified_problems
