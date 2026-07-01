from dataclasses import dataclass, field
from typing import Literal


Role = Literal["system", "user", "assistant", "tool"]


@dataclass(slots=True)
class Message:
    """
    Одно сообщение диалога.
    """

    role: Role
    content: str


@dataclass(slots=True)
class LLMResponse:
    """
    Ответ модели.
    """

    text: str

    model: str

    tokens: int | None = None

    duration: float | None = None


@dataclass(slots=True)
class SessionState:
    """
    Текущее состояние сессии.
    """

    model: str

    temperature: float

    messages: list[Message] = field(default_factory=list)
