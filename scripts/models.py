from dataclasses import dataclass


@dataclass(slots=True)
class Problem:
    """
    Represents a single solved LeetCode problem.
    """

    id: str
    title: str
    difficulty: str
    topics: list[str]
    folder: str
    slug: str
