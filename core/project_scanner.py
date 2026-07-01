import ast
from pathlib import Path


class ProjectScanner:

    def scan(self, path: str | Path) -> dict:

        path = Path(path)

        source = path.read_text(
            encoding="utf-8"
        )

        tree = ast.parse(source)

        result = {
            "file": str(path),
            "imports": [],
            "classes": [],
            "functions": [],
            "entrypoint": False,
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for name in node.names:
                    result["imports"].append(
                        name.name
                    )

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                result["imports"].append(module)

            elif isinstance(node, ast.ClassDef):

                result["classes"].append(
                    node.name
                )

            elif isinstance(node, ast.FunctionDef):

                result["functions"].append(
                    node.name
                )

            elif isinstance(node, ast.If):

                if (
                    isinstance(node.test, ast.Compare)
                    and isinstance(
                        node.test.left,
                        ast.Name,
                    )
                    and node.test.left.id == "__name__"
                ):

                    result["entrypoint"] = True

        return result
