from core.llm import ask
from core.logger import log

print("AI-Studio")
print("Введите exit для выхода.\n")

while True:
    prompt = input(">>> ")

    if prompt.lower() == "exit":
        break

    log("USER: " + prompt)

    answer = ask(prompt)

    log("AI: " + answer)

    print()
    print(answer)
    print()
