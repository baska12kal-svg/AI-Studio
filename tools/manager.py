from tools.registry import ToolRegistry
from tools.result import ToolResult
from tools.tool import Tool
from tools.filesystem import FilesystemTool
from tools.terminal import TerminalTool


class ToolManager:
    """
    Executes registered tools.
    """

    def __init__(self):
        self.registry = ToolRegistry()
        self.register(FilesystemTool())
        self.register(TerminalTool())

    def register(self, tool: Tool) -> None:
        self.registry.register(tool)

    def unregister(self, name: str) -> None:
        self.registry.unregister(name)

    def execute(self, name: str, **kwargs) -> ToolResult:
        tool = self.registry.get(name)

        if tool is None:
            return ToolResult(
                success=False,
                error=f"Tool '{name}' is not registered."
            )

        return tool.execute(**kwargs)

    def list(self) -> list[str]:
        return self.registry.list()
