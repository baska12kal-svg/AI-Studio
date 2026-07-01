from core.project import Project

project = Project()

project.scan()

print()

print(project.stats())

print()

print(project.find_file("llm.py"))

print()

print(project.find_class("Session"))

print()

print(project.find_function("ask"))

print()

print(project.find_import("ollama"))
