import requests

res = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5-coder:7b",
        "prompt": "Напиши функцию факториала на Python"
    }
)

print(res.json()["response"])
