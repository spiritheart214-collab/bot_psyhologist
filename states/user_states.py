"""
Состояния пользователя.
После завершения регистрации - словарь очищается
"""
from enum import Enum


class RegistrationUserStates(Enum):
    """Класс с состояниями пользователя"""

    CONFIRM_VK_NAME = "confirm vk name"
    WAITING_NAME = "waiting name"
    WAITING_SURNAME = "waiting surname"
    WAITING_PHONE = "waiting phone"

user_states = {}


