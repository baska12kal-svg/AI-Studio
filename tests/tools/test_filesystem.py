from pathlib import Path

from tools.filesystem import FilesystemTool


tool = FilesystemTool()

TEST_DIR = Path("tests/tmp")
TEST_FILE = TEST_DIR / "hello.txt"


def cleanup():
    if TEST_DIR.exists():
        for item in TEST_DIR.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                import shutil
                shutil.rmtree(item)

        TEST_DIR.rmdir()

cleanup()


print("MKDIR")

print(
    tool.execute(
        action="mkdir",
        path=str(TEST_DIR)
    )
)

print("WRITE")

print(
    tool.execute(
        action="write",
        path=str(TEST_FILE),
        content="Hello AI Studio!"
    )
)

print("EXISTS")

print(
    tool.execute(
        action="exists",
        path=str(TEST_FILE)
    )
)

print("READ")

print(
    tool.execute(
        action="read",
        path=str(TEST_FILE)
    )
)

print("SIZE")

print(
    tool.execute(
        action="size",
        path=str(TEST_FILE)
    )
)

print("IS_FILE")

print(
    tool.execute(
        action="is_file",
        path=str(TEST_FILE)
    )
)

print("DELETE")

print(
    tool.execute(
        action="delete",
        path=str(TEST_FILE)
    )
)

print("LIST")

print(
    tool.execute(
        action="list",
        path="tests"
    )
)

print("DELETE DIRECTORY")

print(
    tool.execute(
        action="delete",
        path="tests/tmp"
    )
)

print("TOUCH")

print(
    tool.execute(
        action="touch",
        path="tests/tmp/new.txt"
    )
)

print("APPEND")

print(
    tool.execute(
        action="append",
        path="tests/tmp/new.txt",
        content="\nSecond line"
    )
)

print("ABSOLUTE")

print(
    tool.execute(
        action="absolute",
        path="tests/tmp/new.txt"
    )
)

print("PARENT")

print(
    tool.execute(
        action="parent",
        path="tests/tmp/new.txt"
    )
)

print("COPY")

print(
    tool.execute(
        action="copy",
        src="tests/tmp/new.txt",
        dst="tests/tmp/copy.txt"
    )
)

print("MOVE")

print(
    tool.execute(
        action="move",
        src="tests/tmp/copy.txt",
        dst="tests/tmp/moved.txt"
    )
)

print("RENAME")

print(
    tool.execute(
        action="rename",
        path="tests/tmp/moved.txt",
        name="renamed.txt"
    )
)

cleanup()
