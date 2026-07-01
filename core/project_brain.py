from core.project import Project


class ProjectBrain:

    def __init__(self, project: Project):
        self.project = project

    def summary(self) -> str:

        stats = self.project.stats()

        lines = []

        lines.append("=== PROJECT SUMMARY ===")
        lines.append("")

        lines.append(f"Files: {stats['files']}")
        lines.append(f"Python: {stats['python_files']}")
        lines.append(f"Classes: {stats['classes']}")
        lines.append(f"Functions: {stats['functions']}")
        lines.append(f"Imports: {stats['imports']}")

        lines.append("")
        lines.append("Classes:")

        for cls in sorted(self.project.classes):
            lines.append(f"  - {cls}")

        return "\n".join(lines)
