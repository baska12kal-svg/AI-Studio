from core.project import Project
from core.project_brain import ProjectBrain

project = Project()
project.scan()

brain = ProjectBrain(project)

print()
print(brain.summary())
print()
