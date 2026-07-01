from core.project_analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer()

files = analyzer.index()

print()

print(f"FILES: {len(files)}")

print()

for file in files[:10]:
    print(file)
