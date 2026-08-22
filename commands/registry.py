"""Модуль содержит еестр зарегестрированных команд и функция по работе с реестром"""
from typing import Callable, Dict, Optional, Tuple
from vk_bot import MessageContext

_COMMANDS: Dict[str, Callable] = {}  # Реестр


def get_command(context: MessageContext) -> Tuple[str, Optional[str]]:
    """
    Функция ищет введенную пользователем команду в реестре зарегистрированных команд и выполняет.
    """
    command_name = context.text.lower().strip()

    # Если команда не в списке зарегестрированных
    if command_name not in _COMMANDS:
        return f"Неизвестная команда {command_name}. Напишите 'помощь'.", None

    command = _COMMANDS[command_name]

    return command(context)
