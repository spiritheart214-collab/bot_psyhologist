"""Контекст входящего сообщения от пользователя."""
from dataclasses import dataclass

from vk_bot import VKBot


@dataclass(slots=True)
class MessageContext:
    """Хранит данные сообщения и объект бота для его обработки."""
    user_id: int
    text: str
    bot: VKBot
