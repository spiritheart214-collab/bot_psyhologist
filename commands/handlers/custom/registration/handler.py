"""Обработчик сценария регистрации пользователя."""

from vk_bot import MessageContext

from .session import registration_sessions
from .states import RegistrationStates


def handle_confirm_vk_name(context: MessageContext, session) -> None:
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


def handle_name(context: MessageContext, session,) -> None:
    """Обрабатывает ввод имени."""

    session.name = context.text
    session.state = RegistrationStates.WAITING_SURNAME

    context.bot.send_message(
        user_id=context.user_id,
        message="Введите вашу фамилию:"
    )


def handle_surname(context: MessageContext, session) -> None:
    """Обрабатывает ввод фамилии."""

    session.lastname = context.text
    session.state = RegistrationStates.WAITING_PHONE

    context.bot.send_message(
        user_id=context.user_id,
        message="Введите ваш телефон:"
    )


def handle_phone(context: MessageContext, session) -> None:
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

    if session.state == RegistrationStates.CONFIRM_VK_NAME:
        handle_confirm_vk_name(context, session)

    elif session.state == RegistrationStates.WAITING_NAME:
        handle_name(context, session)

    elif session.state == RegistrationStates.WAITING_SURNAME:
        handle_surname(context, session)

    elif session.state == RegistrationStates.WAITING_PHONE:
        handle_phone(context, session)

    return True
