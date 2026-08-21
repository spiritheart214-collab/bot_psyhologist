"""Регистрация пользователя"""
from commands.decorators import command
from keyboards import get_yes_no_menu
from states import RegistrationUserStates, user_states
from vk_bot import MessageContext


@command(["регистрация"])
def register_command(context: MessageContext):
    """Запуск регистрации пользователя"""
    user_states[context.user_id] = RegistrationUserStates.CONFIRM_VK_NAME
    print(user_states)

    user_name = context.bot.get_user_name(user_id=context.user_id)

    message = (f"Я посмотрел ваше имя в профиле в вк.\n"
               f"'{user_name}' ваше настоящее имя или указать другое?")

    return message, get_yes_no_menu()


def handle_registration(context: MessageContext) -> bool:
    """Обрабатывает сообщение пользователя в зависимости от его состояния."""

    if context.user_id not in user_states:
        return False

    state = user_states[context.user_id]

    if state == RegistrationUserStates.WAITING_NAME:
        print(f"Имя: {context.text}")

        user_states[context.user_id] = RegistrationUserStates.WAITING_SURNAME

        context.bot.send_message(
            user_id=context.user_id,
            message="Введите вашу фамилию"
        )

    elif state == RegistrationUserStates.WAITING_SURNAME:
        print(f"Фамилия: {context.text}")

        del user_states[context.user_id]

        context.bot.send_message(
            user_id=context.user_id,
            message="Всё"
        )

    elif state == RegistrationUserStates.CONFIRM_VK_NAME:
        pass

    return True
