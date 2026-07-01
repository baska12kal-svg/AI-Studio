from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def log(text: str):
    with open(LOG_DIR / "latest.log", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%H:%M:%S")
        f.write(f"[{now}] {text}\n")
