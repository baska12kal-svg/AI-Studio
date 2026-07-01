from core.conversation import Conversation

print("AI-Studio")
print("Введите exit для выхода.\n")

conversation = Conversation()

while True:
    prompt = input(">>> ")

    if prompt.lower() == "exit":
        break

    print()
    print(conversation.send(prompt))
    print()
