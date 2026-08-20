"""Модуль по работе с состояниями"""

from .user_register_states import WAITING_NAME, WAITING_SURNAME, user_states
from vk_bot import VKBot, MessageContext


def handle_state(context: MessageContext) -> bool:
    """Обрабатывает сообщение пользователя в зависимости от его состояния."""
    if context.user_id not in user_states:
        return False

    state = user_states[context.user_id]
    if state == WAITING_NAME:
        print(f"Имя: {context.text}")

        user_states[context.user_id] = WAITING_SURNAME
        context.bot.send_message(user_id=context.user_id, message="Введите вашу фамилию")

    elif state == WAITING_SURNAME:
        print(f"Фамилия: {context.text}")

        del user_states[context.user_id]

        context.bot.send_message(user_id=context.user_id, message="Всё")

    return True
