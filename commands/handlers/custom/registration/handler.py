"""Обработчик сценария регистрации пользователя."""

from logger import logger
from vk_bot import MessageContext

from .session import registration_sessions, RegistrationSession
from .states import RegistrationStates


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
    """Обрабатывает ввод телефона и завершает регистрацию."""

    session.phone = context.text

    print(session)

    context.bot.send_message(
        user_id=context.user_id,
        message="Вы зарегистрированы!"
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

    new_state = session.state if context.user_id in registration_sessions else None

    logger.info(
        f"Переход состояния | "
        f"Пользователь: {context.bot.get_user_name(context.user_id)} [{context.user_id}] |\n "
        f"\t{old_state.name} -> "
        f"{new_state.name if new_state else '[Завершение регистрации!]'}"
    )

    return True
