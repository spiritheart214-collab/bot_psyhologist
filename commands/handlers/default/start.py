from typing import Tuple

from commands.decorators import command
from keyboards import get_register_menu


@command(["начать"])
def start_command() -> Tuple[str, str]:
    message = ("Привет. Я твой бот - помощник, я буду помагать тебе делать запись на встречу.\n"
               "И это все обо мне! \n"
               "Если ты тут впервые, то нажми на 'регестрация', чтобы я тоже о тебе узнал :3\n"
               "Или на 'помощь', чтобы посмотреть остальные команды!")
    keyboard = get_register_menu()

    return message, keyboard
