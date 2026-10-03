"""Временные данные пользователя во время регистрации."""
from dataclasses import dataclass
from typing import Optional

from .states import RegistrationStates


@dataclass
class RegistrationSession:
    """Хранит данные пользователя до завершения регистрации."""

    state: RegistrationStates
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
    request: Optional[str] = None

# словарь с временными сессиями
registration_sessions: dict[int, RegistrationSession] = {}
