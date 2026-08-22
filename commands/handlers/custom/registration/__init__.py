"""Сценарий регистрации пользователя."""

from .command import register_command
from .handler import handle_registration

__all__ = [
    "register_command",
    "handle_registration",
]