"""Сценарий регистрации пользователя."""

from commands.decorators import command
from keyboards import get_yes_no_menu
from vk_bot import MessageContext

from .session import RegistrationSession, registration_sessions
from .states import RegistrationStates


@command(["регистрация"])
def register_command(context: MessageContext):
    """Запускает регистрацию пользователя."""

    registration_sessions[context.user_id] = RegistrationSession(state=RegistrationStates.CONFIRM_VK_NAME)

    user_name = context.bot.get_user_name(
        user_id=context.user_id
    )

    message = (
        "Я посмотрел ваше имя в профиле в ВК.\n"
        f"'{user_name}' — ваше настоящее имя ?"
    )

    return message, get_yes_no_menu()
