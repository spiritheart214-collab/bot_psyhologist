"""Модуль по работе с состояниями"""

from .user_register_states import  WAITING_NAME, WAITING_SURNAME, user_states
from vk_bot import VKBot


def handle_state(user_id: int, user_message: str, vk_bot: VKBot) -> bool:
    """Обрабатывает сообщение пользователя в зависимости от его состояния."""
    if user_id in user_states:

        state = user_states[user_id]

        if state == WAITING_NAME:
            print(f"Имя: {user_message}")

            user_states[user_id] = WAITING_SURNAME

            vk_bot.send_message(user_id=user_id, message="Введите вашу фамилию")

        elif state == WAITING_SURNAME:
            print(f"Фамилия: {user_message}")

            del user_states[user_id]

            vk_bot.send_message(user_id=user_id, message="Всё")

        return True
    else:
        return False
