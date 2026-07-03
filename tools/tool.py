from abc import ABC, abstractmethod

from tools.result import ToolResult


class Tool(ABC):
    """
    Base class for every AI Studio tool.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Tool unique name."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        """Execute tool."""
        raise NotImplementedError
