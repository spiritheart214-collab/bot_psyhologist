"""Модуль содержит еестр зарегестрированных команд и функция по работе с реестром"""
from typing import Callable, Dict, Optional, Tuple

_COMMANDS: Dict[str, Callable] = {} # Реестр


def get_command(name: str) -> Tuple[str, Optional[str]]:
    """
    Функция ищет введенную пользователем команду в реестре зарегистрированных команд и возвращает соответствующий ответ
    """
    name = name.lower().strip()
    if name in _COMMANDS:
        return _COMMANDS[name]()
    return f"Неизвестная команда {name}. Напишите 'помощь'.", None
