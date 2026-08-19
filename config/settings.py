"""Модуль конфигурации бота"""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from config.config_exaptions import ValueNotLoadedError
from logger import logger


@dataclass(frozen=True, slots=True)
class Config:
    """Конфигурация бота"""
    VK_TOKEN: Optional[str] = None

    def __post_init__(self):
        """Валидация после создания"""
        try:
            self._is_env_variables_exists()
        except ValueNotLoadedError as error:
            logger.critical(f"Завершение работы по ошибке: {error}!")
            exit(f"Завершение работы по ошибке: {error}!")
        else:
            logger.success("Все переменные виртуального окружения загруженны успешно!")

    def _is_env_variables_exists(self):
        if not self.VK_TOKEN:
            raise ValueNotLoadedError(variable="VK_TOKEN")


def load_config() -> Config:
    """Загрузить конфигурацию из .env и создание обьекта класса конфигураций при успешном создании"""
    # Находим корень проекта
    root_directory = Path(__file__).parent.parent
    env_path = root_directory / '.env'

    # Проверяем существование .env файла
    logger.debug(f"Поиск .env по пути: {env_path}")
    if not env_path.exists():
        logger.critical(f"Файл .env не найден по пути: {env_path}")
        logger.info("Завершение работы!")
        exit("Завершение работы!")
    else:
        logger.info("Файл .env найден !")

    # Загружаем переменные из .env и забираем переменне
    logger.debug("Загрузка переменных окружения ...")
    load_dotenv(env_path)

    # Получаем токен
    token = os.getenv("VK_TOKEN")

    # Создаем объект (__post_init__ сам проверит)
    return Config(VK_TOKEN=token)


if __name__ == '__main__':
    config = load_config()
