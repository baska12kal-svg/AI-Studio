from core.project_scanner import ProjectScanner

scanner = ProjectScanner()

result = scanner.scan(
    "core/session.py"
)

print()

for key, value in result.items():
    print(f"{key}: {value}")

print()
