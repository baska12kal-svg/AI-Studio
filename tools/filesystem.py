import shutil
from pathlib import Path

from tools.result import ToolResult
from tools.tool import Tool


class FilesystemTool(Tool):

    @property
    def name(self) -> str:
        return "filesystem"

    def execute(self, action: str, **kwargs) -> ToolResult:
        try:

            if action == "exists":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=path.exists()
                )

            elif action == "is_file":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=path.is_file()
                )

            elif action == "is_dir":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=path.is_dir()
                )

            elif action == "mkdir":
                path = Path(kwargs["path"])

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                return ToolResult(
                    success=True,
                    output=f"Directory '{path}' created."
                )

            elif action == "touch":
                path = Path(kwargs["path"])

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                path.touch(exist_ok=True)

                return ToolResult(
                    success=True,
                    output=f"File '{path}' created."
                )

            elif action == "read":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    output=path.read_text(
                        encoding="utf-8"
                    )
                )

            elif action == "write":
                path = Path(kwargs["path"])

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                path.write_text(
                    kwargs["content"],
                    encoding="utf-8"
                )

                return ToolResult(
                    success=True,
                    output=f"Written '{path}'."
                )

            elif action == "append":
                path = Path(kwargs["path"])

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                with path.open(
                    "a",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        kwargs["content"]
                    )

                return ToolResult(
                    success=True,
                    output=f"Appended '{path}'."
                )

            elif action == "delete":
                path = Path(kwargs["path"])

                if not path.exists():
                    return ToolResult(
                        success=False,
                        error=f"'{path}' does not exist."
                    )

                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()

                return ToolResult(
                    success=True,
                    output=f"Deleted '{path}'."
                )

            elif action == "list":
                path = Path(kwargs["path"])

                if not path.exists():
                    return ToolResult(
                        success=False,
                        error=f"Directory '{path}' does not exist."
                    )

                if not path.is_dir():
                    return ToolResult(
                        success=False,
                        error=f"'{path}' is not a directory."
                    )

                return ToolResult(
                    success=True,
                    data=[item.name for item in path.iterdir()]
                )
              

            elif action == "copy":
                src = Path(kwargs["src"])
                dst = Path(kwargs["dst"])

                dst.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                shutil.copy2(src, dst)

                return ToolResult(
                    success=True,
                    output=f"Copied '{src}' -> '{dst}'."
                )

            elif action == "move":
                src = Path(kwargs["src"])
                dst = Path(kwargs["dst"])

                dst.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                shutil.move(
                    str(src),
                    str(dst)
                )

                return ToolResult(
                    success=True,
                    output=f"Moved '{src}' -> '{dst}'."
                )

            elif action == "rename":
                path = Path(kwargs["path"])
                new_name = kwargs["name"]

                destination = path.with_name(
                    new_name
                )

                path.rename(destination)

                return ToolResult(
                    success=True,
                    output=f"Renamed to '{destination.name}'."
                )

            elif action == "size":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=path.stat().st_size
                )

            elif action == "absolute":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=str(
                        path.resolve()
                    )
                )

            elif action == "parent":
                path = Path(kwargs["path"])

                return ToolResult(
                    success=True,
                    data=str(
                        path.parent
                    )
                )

            return ToolResult(
                success=False,
                error=f"Unknown action '{action}'."
            )

        except Exception as error:

            return ToolResult(
                success=False,
                error=str(error)
            )
