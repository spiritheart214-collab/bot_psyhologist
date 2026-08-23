from vk_bot import MessageContext
from logger import log_message
from .registry import get_command
from .dispatcher import handle_active

__all__ = ["get_command", "handle_active"]


@log_message
def handle_massage(context: MessageContext) -> None:
    """Отлов сообщения пользователя и выбор сценария: cостояние / выбор команды выполнения"""

    # Если пользователь находится в каком-то состоянии
    if handle_active(context=context):
        # Очень важно: Если состояние было найдено, дальше get_command() не вызываем.
        return None

    message, keyboard = get_command(context=context)
    context.bot.send_message(user_id=context.user_id, message=message, keyboard=keyboard)
