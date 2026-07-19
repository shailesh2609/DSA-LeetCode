import os
import re
import subprocess

def problem_number(folder):
    match = re.match(r"(\d+)", folder)

    if match:
        return int(match.group(1))

    return -1
    

def extract_problem_id(folder):
    """
    Example:

    3-longest-substring-without-repeating-characters

    →

    3
    """

    match = re.match(r"(\d+)", folder)

    if match:
        return match.group(1)

    return None

def folder_to_slug(folder):
    """
    Example:

    3-longest-substring-without-repeating-characters

    →

    longest-substring-without-repeating-characters
    """

    return folder.split("-", 1)[1]


def problem_title(folder):
    """
    Convert folder name to readable title.

    Example:

    704-binary-search

    →

    Binary Search
    """

    title = re.sub(r"^\d+-", "", folder)

    title = title.replace("-", " ")

    return title.title()

def rename_problem_folder(old_folder, new_folder):
    """
    Rename a problem folder using git so that
    Git history is preserved.
    """

    subprocess.run(
        [
            "git",
            "mv",
            old_folder,
            new_folder,
        ],
        check=True,
    )
