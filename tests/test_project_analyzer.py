from core.project_analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer()

for line in analyzer.tree():
    print(line)
