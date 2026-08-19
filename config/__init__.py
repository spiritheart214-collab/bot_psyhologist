"""Настройка пакета"""
from .settings import load_config

bot_config = load_config()


__all__ = ["bot_config"]
