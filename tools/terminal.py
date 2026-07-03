import subprocess
from pathlib import Path

from tools.result import ToolResult
from tools.tool import Tool


class TerminalTool(Tool):

    @property
    def name(self) -> str:
        return "terminal"

    def execute(self, action: str, **kwargs) -> ToolResult:

        if action != "run":
            return ToolResult(
                success=False,
                error=f"Unknown action '{action}'."
            )

        command = kwargs.get("command")

        if command is None:
            return ToolResult(
                success=False,
                error="Missing 'command'."
            )

        cwd = kwargs.get("cwd")
        timeout = kwargs.get("timeout", 30)

        if cwd is not None:
            cwd = str(Path(cwd))

        shell = isinstance(command, str)

        try:

            process = subprocess.run(
                command,
                cwd=cwd,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            stdout = process.stdout.strip()
            stderr = process.stderr.strip()

            return ToolResult(
                success=process.returncode == 0,
                output=stdout,
                error=stderr if stderr else None,
                data={
                    "returncode": process.returncode, 
                },
            )

        except subprocess.TimeoutExpired:

            return ToolResult(
                success=False,
                error=f"Command timed out after {timeout} seconds."
            )

        except FileNotFoundError:

            return ToolResult(
                success=False,
                error="Command not found."
            )

        except Exception as error:

            return ToolResult(
                success=False,
                error=str(error)
            )
