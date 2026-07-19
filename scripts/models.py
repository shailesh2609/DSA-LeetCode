from dataclasses import dataclass


@dataclass(slots=True)
class Problem:
    frontend_id: str
    title: str
    difficulty: str
    topics: list[str]
    folder: str
    slug: str
