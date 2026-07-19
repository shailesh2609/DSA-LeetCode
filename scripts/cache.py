import os
import json

CACHE_DIR = ".cache"
CACHE_FILE = os.path.join(CACHE_DIR, "topics.json")


def load_cache():
    """
    Load cached LeetCode metadata.
    """

    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache):
    """
    Save metadata cache.
    """

    os.makedirs(CACHE_DIR, exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

    print(f"Saved {len(cache)} problems to cache.")
