import os
import subprocess

from utils import problem_number

def get_problem_folders():
    """
    Returns all LeetCode problem folders.
    """
    IGNORE = {
        ".git",
        ".github",
        ".cache",
        "__pycache__",
        "scripts",
        "docs",
        ".vscode",
    }

    folders = []

    for item in os.listdir("."):

        if not os.path.isdir(item):
            continue

        if item in IGNORE:
            continue

        folders.append(item)
            
    folders.sort(key=problem_number)
    return folders

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
    
