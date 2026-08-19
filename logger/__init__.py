"""Настройка пакета"""
from .logger_setup import setup_logger

logger = setup_logger()

__all__ = ["logger"]