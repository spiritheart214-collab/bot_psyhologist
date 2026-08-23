"""Настройка логгера для всего проекта"""
import sys
from pathlib import Path

from loguru import logger


def setup_logger():
    """
    Настройка глобального логгера.

    Returns:
        logger: Настроенный логгер
    """
    # Создаем папку для логов
    root_directory = Path(__file__).parent.parent  # 👈 Это Path
    logs_dir = root_directory / "logs"
    logs_dir.mkdir(exist_ok=True)

    # Удаляем стандартный обработчик
    logger.remove()

    # === Вывод в консоль ===
    logger.add(
        sys.stdout,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        colorize=True,
        level="DEBUG",
        backtrace=True,
        diagnose=True
    )

    # === Запись в файл (все уровни) ===
    logger.add(
        logs_dir / "bot_{time:YYYY-MM-DD}.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="1 day",  # Новый файл каждый день
        retention="30 days",  # Хранить 30 дней
        level="DEBUG",  # В файл все уровни
        encoding="utf-8"
    )

    # === Только ошибки в отдельный файл ===
    logger.add(
        logs_dir / "errors_{time:YYYY-MM-DD}.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="1 day",
        retention="30 days",
        level="ERROR",
        encoding="utf-8"
    )

    logger.debug(f"Логгер инициализирован в {Path(__file__)}")
    return logger


logger = setup_logger()
