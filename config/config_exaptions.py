"""Исключения / ошибки конфигураций"""
from typing import Optional

from logger import logger


class ConfigError(Exception):
    """Общий класс ошибок для конфигураций"""

    def __init__(self, message: str) -> None:
        """Передает кастомное сообщение базовому классу"""
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """Вывод ошибки"""
        message = f"{self.__class__.__name__}: {self.message}"
        return message


class ValueNotLoadedError(ConfigError):
    """Не загруженна переменная окружения"""

    def __init__(self, variable: Optional[str] = None, message: str = "переменная не загруженна") -> None:
        """
        Составление ошибки
        :param variable: не найденная переменная
        :param message: сообщение об ошибке. Если не заполнить параметр, то будет сообщение по умолчанию
        """

        if variable:
            message = f"переменная {variable} не загруженна"
            logger.critical(f"ValueNotLoadedError: {message}")
        else:
            logger.critical(f"ValueNotLoadedError: {message}")
        super().__init__(message=message)
