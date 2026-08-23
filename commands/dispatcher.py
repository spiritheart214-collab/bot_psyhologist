"""Маршрутизация активных сценариев пользователя."""

from vk_bot import MessageContext

from .handlers.custom.registration import handle_registration

# Кортеж сценариев
_ACTIVE_HANDLERS = (
    handle_registration,
)


def handle_active(context: MessageContext) -> bool:
    """
    Передаёт сообщение пользователя активному сценарию.
    Возвращает True, если сообщение было обработано.
    """
    for handler in _ACTIVE_HANDLERS:
        if handler(context):
            return True

    return False

