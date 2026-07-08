import os
import re
import subprocess
from pathlib import Path

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

def get_last_commit_timestamp(folder):
    """
    Returns the Unix timestamp of the latest commit
    that modified the given folder.
    """

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "-1",
                "--format=%ct",
                "--",
                folder,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        timestamp = result.stdout.strip()

        if timestamp:
            return int(timestamp)

    except Exception:
        pass

    return 0
    
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
