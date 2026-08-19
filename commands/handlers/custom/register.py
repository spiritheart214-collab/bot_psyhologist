"""Регистрация пользователя"""
from commands.decorators import command
from states import WAITING_NAME, user_states


@command(["регистрация"])
def register_command(user_id: int):
    """Запуск регистрации пользователя"""

    user_states[user_id] = WAITING_NAME
    return "Введите ваше имя", None
