from core.types import Message
from core.types import SessionState

from core.config import config
from core.prompt_loader import load_prompt


class Session:
    """
    Управляет текущим диалогом.
    """

    def __init__(self):
        self.state = SessionState(
            model=config.model,
            temperature=config.temperature,
        )

        self.add_system(
            load_prompt("system")
        )

    def add_system(self, text: str):
        self.state.messages.append(
            Message(
                role="system",
                content=text,
            )
        )

    def add_user(self, text: str):
        self.state.messages.append(
            Message(
                role="user",
                content=text,
            )
        )

    def add_assistant(self, text: str):
        self.state.messages.append(
            Message(
                role="assistant",
                content=text,
            )
        )

    def clear(self):
        """
        Очищает историю,
        но сохраняет system prompt.
        """

        system = self.state.messages[0]

        self.state.messages.clear()

        self.state.messages.append(system)

    def messages(self):
        return self.state.messages
