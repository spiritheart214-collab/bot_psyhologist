"""Сценарий работы с запросом пользователя."""

from commands.decorators import command
from logger import log_command
from vk_bot import MessageContext


def start_request(context: MessageContext) -> tuple[str, None]:
    """Запускает ввод запроса пользователя."""

    return "Введите запрос:", None


@command(["запрос"])
@log_command
def request_command(context: MessageContext):
    """Запускает сценарий ввода запроса."""

    return start_request(context)