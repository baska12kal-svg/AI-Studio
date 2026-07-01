from core.session import Session

session = Session()

session.add_user("Привет")

session.add_assistant("Здравствуйте!")

for message in session.messages():
    print(message)
