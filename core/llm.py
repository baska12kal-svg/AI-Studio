from ollama import Client
from core.config import config

client = Client(host=config.host)


def ask(prompt: str) -> str:
    response = client.generate(
        model=config.model,
        prompt=prompt,
        options={
            "temperature": config.temperature,
        },
    )

    return response["response"].strip()
