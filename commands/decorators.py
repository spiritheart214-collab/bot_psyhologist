# commands/decorators.py
"""Команды бота с декораторами"""
from typing import List

from .registry import _COMMANDS


# TODO доделать декоратор
def command(names: List[str]):
    """Декоратор для регистрации команд"""

    def wrapper(func):
        for name in names:
            _COMMANDS[name.lower()] = func
        return func

    return wrapper
