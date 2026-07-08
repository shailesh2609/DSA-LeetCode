import os
import re


def get_problem_folders():
    """
    Returns all LeetCode problem folders.
    """

    folders = []

    for item in os.listdir("."):

        if os.path.isdir(item):

            if item.startswith("."):
                continue

            if item in ["scripts", "__pycache__"]:
                continue

            folders.append(item)

    return folders


def problem_number(folder):
    """
    Extract problem number.

    Example:
    704-binary-search -> 704
    """

    match = re.match(r"(\d+)", folder)

    if match:
        return int(match.group(1))

    return -1


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
