"""
Состояния пользователя.
После завершения регистрации - словарь очищается
"""
from enum import Enum


class RegistrationStates(Enum):
    """Класс с состояниями пользователя"""

    CONFIRM_VK_NAME = "confirm_vk_name"
    WAITING_NAME = "waiting_name"
    WAITING_SURNAME = "waiting_surname"
    WAITING_PHONE = "waiting_phone"
    WAITING_REQUEST = "waiting_request"
    WAITING_REQUEST_TEXT = "waiting_request_text"
