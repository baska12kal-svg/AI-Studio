from pathlib import Path
from core.project_types import ProjectFile


IGNORE = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    ".idea",
    ".vscode",
}


class ProjectAnalyzer:
    def __init__(self, root: str = "."):
        self.root = Path(root).resolve()

    def tree(self) -> list[str]:
        result = []
        self._walk(self.root, result, 0)
        return result

    def index(self) -> list[ProjectFile]:
        """
        Возвращает информацию обо всех файлах проекта.
        """

        files = []
        self._index_walk(self.root, files)
        return files

    def _walk(
        self,
        directory: Path,
        result: list[str],
        level: int,
    ):
        entries = sorted(
            directory.iterdir(),
            key=lambda p: (
                p.is_file(),
                p.name.lower(),
            ),
        )

        for entry in entries:

            if entry.name in IGNORE:
                continue

            indent = "    " * level

            if entry.is_dir():

                result.append(f"{indent}{entry.name}/")

                self._walk(
                    entry,
                    result,
                    level + 1,
                )

            else:

                result.append(f"{indent}{entry.name}")

    def _index_walk(
        self,
        directory: Path,
        files: list[dict],
    ):
        entries = sorted(
            directory.iterdir(),
            key=lambda p: (
                p.is_file(),
                p.name.lower(),
            ),
        )

        for entry in entries:

            if entry.name in IGNORE:
                continue

            if entry.is_dir():

                self._index_walk(
                    entry,
                    files,
                )

            else:

                stat = entry.stat()

                files.append(
                   ProjectFile(
                     name=entry.name,
                     path=str(entry.relative_to(self.root)),
                     suffix=entry.suffix,
                     size=stat.st_size,
                    )                
                )

