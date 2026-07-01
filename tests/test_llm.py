from ollama import Client
import time

print("=== START ===")

client = Client(host="http://127.0.0.1:11434")

print("Client OK")

start = time.time()

response = client.generate(
    model="qwen2.5-coder:7b",
    prompt="Привет"
)

print("Elapsed:", round(time.time() - start, 2), "sec")

print(response["response"])
