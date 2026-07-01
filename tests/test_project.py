from core.project import Project

project = Project()

project.scan()

print()

print("Python files:", len(project.python_files))

print("Classes:", len(project.classes))

print("Functions:", len(project.functions))

print("Imports:", len(project.imports))

print()

print(project.classes)

print()

print(project.functions[:20])
