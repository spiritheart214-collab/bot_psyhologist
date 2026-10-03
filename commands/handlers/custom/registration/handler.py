"""Обработчик сценария регистрации пользователя."""
from keyboards import get_yes_no_menu
from logger import logger
from vk_bot import MessageContext

from database import create_user, create_user_request, find_user

from .session import registration_sessions, RegistrationSession
from .states import RegistrationStates
from ..request import start_request


def handle_confirm_vk_name(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает подтверждение имени из VK."""

    if context.text == "да":
        user_name = context.bot.get_user_name(
            user_id=context.user_id
        )

        name, lastname = user_name.split(maxsplit=1)

        session.name = name
        session.lastname = lastname
        session.state = RegistrationStates.WAITING_PHONE

        context.bot.send_message(
            user_id=context.user_id,
            message="Введите ваш телефон:"
        )

    else:
        session.state = RegistrationStates.WAITING_NAME

        context.bot.send_message(
            user_id=context.user_id,
            message="Введите ваше имя:"
        )


def handle_name(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает ввод имени."""

    session.name = context.text
    session.state = RegistrationStates.WAITING_SURNAME

    context.bot.send_message(
        user_id=context.user_id,
        message="Введите вашу фамилию:"
    )


def handle_surname(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает ввод фамилии."""

    session.lastname = context.text
    session.state = RegistrationStates.WAITING_PHONE

    context.bot.send_message(
        user_id=context.user_id,
        message="Введите ваш телефон:"
    )


def handle_phone(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает ввод телефона"""

    session.phone = context.text
    session.state = RegistrationStates.WAITING_REQUEST

    context.bot.send_message(
        user_id=context.user_id,
        message="Желаете ввести запрос сейчас?",
        keyboard=get_yes_no_menu()
    )

    create_user(
        vk_id=context.user_id,
        name=session.name,
        surname=session.lastname,
        phone=session.phone
    )


def handle_request_yes_no_choice(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает ввод запроса"""

    user_choice = context.text

    if user_choice == "нет":
        context.bot.send_message(
            user_id=context.user_id,
            message="Вы зарегистрированы!\nЗапрос всегда можно вести позднее."
        )
        del registration_sessions[context.user_id]
    else:
        message, keyboard = start_request(context)

        session.state = RegistrationStates.WAITING_REQUEST_TEXT

        context.bot.send_message(
            user_id=context.user_id,
            message=message,
            keyboard=keyboard
        )


def handle_request_text(context: MessageContext, session: RegistrationSession) -> None:
    """Обрабатывает ввод запроса, завершает регистрацию."""
    context.bot.send_message(
        user_id=context.user_id,
        message="Вы зарегистрированы!"
    )

    user = find_user(context.user_id)
    create_user_request(
        user_id=user,
        request=context.text
    )

    del registration_sessions[context.user_id]


def handle_registration(context: MessageContext) -> bool:
    """Обрабатывает сообщение пользователя в рамках регистрации."""

    session = registration_sessions.get(context.user_id)

    if session is None:
        return False

    old_state = session.state

    if session.state == RegistrationStates.CONFIRM_VK_NAME:
        handle_confirm_vk_name(context, session)

    elif session.state == RegistrationStates.WAITING_NAME:
        handle_name(context, session)

    elif session.state == RegistrationStates.WAITING_SURNAME:
        handle_surname(context, session)

    elif session.state == RegistrationStates.WAITING_PHONE:
        handle_phone(context, session)

    elif session.state == RegistrationStates.WAITING_REQUEST:
        handle_request_yes_no_choice(context, session)

    elif session.state == RegistrationStates.WAITING_REQUEST_TEXT:
        handle_request_text(context, session)

    new_state = session.state if context.user_id in registration_sessions else None

    logger.info(
        f"Переход состояния | "
        f"Пользователь: {context.bot.get_user_name(context.user_id)} [{context.user_id}] |\n "
        f"\t{old_state.name} -> "
        f"{new_state.name if new_state else '[Завершение регистрации!]'}"
    )

    return True
