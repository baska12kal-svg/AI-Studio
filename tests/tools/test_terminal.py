from tools.manager import ToolManager


manager = ToolManager()


print("PWD")
print(
    manager.execute(
        "terminal",
        action="run",
        command="pwd",
    )
)

print()


print("LS")
print(
    manager.execute(
        "terminal",
        action="run",
        command="ls",
    )
)

print()


print("PYTHON VERSION")
print(
    manager.execute(
        "terminal",
        action="run",
        command="python --version",
    )
)

print()


print("INVALID COMMAND")
print(
    manager.execute(
        "terminal",
        action="run",
        command="aaaaaaaaaaaaaaaa",
    )
)
