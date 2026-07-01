from core.types import Message
from core.types import SessionState


session = SessionState(
    model="qwen2.5-coder:7b",
    temperature=0.2,
)

session.messages.append(
    Message(
        role="user",
        content="Привет"
    )
)

print(session)
