from dataclasses import dataclass


@dataclass(slots=True)
class ProjectFile:
    name: str
    path: str
    suffix: str
    size: int
