"""Регистрация пользователя"""
from commands.decorators import command


@command(["регистрация"])
def register_command():
    message = "регистрация"

    return message, None
