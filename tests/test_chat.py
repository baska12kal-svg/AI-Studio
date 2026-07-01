from core.llm import ask
from core.session import Session

session = Session()

session.add_user("Привет!")

response = ask(session)

print()
print(response.text)
print()

print("----- HISTORY -----")

for message in session.messages():
    print(message)
