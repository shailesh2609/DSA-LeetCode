from graphql import fetch_problem_metadata

from utils import (
    get_problem_folders,
    extract_problem_id,
    folder_to_slug,
    rename_problem_folder,
)


def verify_problem_folders():
    """
    Verify every problem folder against the official
    LeetCode frontend ID.

    If LeetSync created an incorrect folder name,
    rename it using git mv.
    """

    print("\nVerifying problem folders...\n")

    for folder in get_problem_folders():

        slug = folder_to_slug(folder)

        metadata = fetch_problem_metadata(slug)

        if metadata is None:
            print(f"Skipping {folder}")
            continue

        folder_id = extract_problem_id(folder)

        official_id = metadata["questionFrontendId"]

        if folder_id == official_id:
            continue

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

    print("Folder verification complete.\n")
