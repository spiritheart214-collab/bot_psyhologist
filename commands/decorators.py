# commands/decorators.py
"""Команды бота с декораторами"""
from typing import List

from colorama import Fore

from logger import logger
from .registry import _COMMANDS


def command(names: List[str]):
    """Декоратор для регистрации команд"""

    def decorator(func):
        for name in names:
            logger.debug(f"Регистрация команды: {Fore.LIGHTMAGENTA_EX + name}")
            _COMMANDS[name.lower()] = func
        return func

    return decorator
