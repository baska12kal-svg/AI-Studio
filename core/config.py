from pathlib import Path
import yaml

CONFIG_PATH = Path("config/config.yaml")


class Config:
    def __init__(self):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        self.host = cfg["host"]
        self.model = cfg["model"]
        self.temperature = cfg["temperature"]
        self.timeout = cfg["timeout"]
        self.max_tokens = cfg["max_tokens"]
        self.logging = cfg["logging"]


config = Config()
