from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ToolResult:
    """
    Result returned by every tool.
    """

    success: bool
    output: str = ""
    error: str | None = None
    data: Any = None
