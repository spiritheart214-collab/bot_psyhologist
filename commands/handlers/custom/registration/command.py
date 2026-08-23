"""Сценарий регистрации пользователя."""

from commands.decorators import command
from keyboards import get_yes_no_menu
from vk_bot import MessageContext
from logger import logger, log_command

from .session import RegistrationSession, registration_sessions
from .states import RegistrationStates


@command(["регистрация"])
@log_command
def register_command(context: MessageContext):
    """Запускает регистрацию пользователя."""

    registration_sessions[context.user_id] = RegistrationSession(state=RegistrationStates.CONFIRM_VK_NAME)
    logger.info(f"Начало регистрации для {context.bot.get_user_name(context.user_id)} [{context.user_id}] "
                f"| установка состояния {registration_sessions[context.user_id].state}")

    user_name = context.bot.get_user_name(
        user_id=context.user_id
    )

    message = (
        "Я посмотрел ваше имя в профиле в ВК.\n"
        f"'{user_name}' — ваше настоящее имя ?"
    )

    return message, get_yes_no_menu()
