"""Подсказки по командам"""
from commands.guard import is_user_exist
from commands.decorators import command
from logger import log_command
from vk_bot import MessageContext


@command(["помощь"])
@is_user_exist
@log_command
def help_command(context: MessageContext):
    """Выводит список доступных команд"""
    message = ("КОМАНДЫ: \n"
               "Начать - приветсвие\n"
               "Регистрация - регистрация в боте\n")

    return message, None
