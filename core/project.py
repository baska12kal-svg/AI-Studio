from core.project_analyzer import ProjectAnalyzer
from core.project_scanner import ProjectScanner


class Project:
    """
    Полная модель проекта.
    """

    def __init__(self, root: str = "."):

        self.root = root

        self.analyzer = ProjectAnalyzer(root)

        self.scanner = ProjectScanner()

        self.tree = []

        self.files = []

        self.classes = []

        self.functions = []

        self.imports = []

    def scan(self):

        self.tree = self.analyzer.tree()

        self.files = self.analyzer.index()

        self.classes.clear()

        self.functions.clear()

        self.imports.clear()

        for file in self.files:

            if file.suffix != ".py":
                continue

            info = self.scanner.scan(
                file.path
            )

            self.classes.extend(
                info["classes"]
            )

            self.functions.extend(
                info["functions"]
            )

            self.imports.extend(
                info["imports"]
            )

    @property
    def python_files(self):

        return [
            file
            for file in self.files
            if file.suffix == ".py"
        ]

    def find_file(self, name: str):

        for file in self.files:

            if file.name == name:
                return file

        return None

    def find_class(self, name: str):

        return name if name in self.classes else None

    def find_function(self, name: str):

        return name if name in self.functions else None

    def find_import(self, name: str):

        for module in self.imports:

            if name in module:
                return module

        return None

    def stats(self):

        return {
            "files": len(self.files),
            "python_files": len(self.python_files),
            "classes": len(self.classes),
            "functions": len(self.functions),
            "imports": len(self.imports),
        }
