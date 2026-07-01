from ollama import Client

client = Client(host="http://127.0.0.1:11434")

response = client.chat(
    model="qwen2.5-coder:7b",
    messages=[
        {
            "role": "user",
            "content": "Привет"
        }
    ]
)

print(response["message"]["content"])
