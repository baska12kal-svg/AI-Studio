from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROMPTS_DIR = BASE_DIR / "prompts"


def load_prompt(name: str) -> str:
    """
    Загружает markdown-промпт.

    Пример:
        load_prompt("system")
        load_prompt("coder")
    """

    file = PROMPTS_DIR / f"{name}.md"

    if not file.exists():
        raise FileNotFoundError(
            f"Prompt '{name}' не найден: {file}"
        )

    return file.read_text(
        encoding="utf-8"
    ).strip()
