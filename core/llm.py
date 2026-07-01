from ollama import Client

HOST = "http://127.0.0.1:11434"
MODEL = "qwen2.5-coder:7b"

client = Client(host=HOST)


def ask(prompt: str) -> str:
    response = client.generate(
        model=MODEL,
        prompt=prompt,
        options={
            "temperature": 0.2
        }
    )

    return response["response"].strip()
