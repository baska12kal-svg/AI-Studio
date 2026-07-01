from ollama import Client

from core.config import config
from core.session import Session
from core.types import LLMResponse

client = Client(host=config.host)


def ask(session: Session) -> LLMResponse:
    messages = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in session.messages()
    ]

    response = client.chat(
        model=config.model,
        messages=messages,
        options={
            "temperature": config.temperature,
        },
    )

    text = response["message"]["content"].strip()

    session.add_assistant(text)

    return LLMResponse(
        text=text,
        model=config.model,
    )
