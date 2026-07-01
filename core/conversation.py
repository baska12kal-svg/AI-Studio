from core.session import Session
from core.llm import ask
from core.logger import log


class Conversation:
    """
    Управляет текущим разговором.
    """

    def __init__(self):
        self.session = Session()

    def send(self, text: str) -> str:
        """
        Отправляет сообщение модели.
        """

        self.session.add_user(text)

        log(f"USER: {text}")

        response = ask(self.session)

        log(f"AI: {response.text}")

        return response.text

    def clear(self):
        """
        Начать новый разговор.
        """

        self.session.clear()
