"""Настройка пакета"""
from .logger_setup import logger
from .bot_decorators import log_message, log_command, log_function, log_create_request, log_created_user

__all__ = ["logger", "log_message", "log_command", "log_function", "log_create_request", "log_created_user"]
