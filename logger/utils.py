from io import StringIO
from typing import  Any, Dict, TYPE_CHECKING

from rich.console import Console

from .logger_setup import logger
if TYPE_CHECKING: from vk_bot import MessageContext


def _extract_context(*args, **kwargs) -> "MessageContext":
    """Из аргов или кваргов извлекает контекст сообщения пользователя"""
    if kwargs:
        context = kwargs["context"]
    else:
        context = args[0]

    return context


def _args_to_str(arguments: tuple) -> str:
    """
    Форматирует аргументы для логирования.
    Автоматически пропускает self для методов класса.
    """
    if not arguments:
        return ""

    # Если первый аргумент похож на self (экземпляр класса)
    # и это не единственный аргумент - пропускаем его
    if (len(arguments) > 0 and
            hasattr(arguments[0], '__class__') and
            not isinstance(arguments[0], type)):  # Проверяем что это не сам класс
        # Скорее всего это self, пропускаем
        args_to_format = arguments[1:]
    else:
        args_to_format = arguments

    if not args_to_format:
        return ""

    # Форматируем аргументы
    result = []
    for arg in args_to_format:
        if isinstance(arg, str):
            result.append(f"'{arg}'")
        else:
            result.append(str(arg))

    return ", ".join(result)


def _kwargs_to_str(keyword_args: Dict[str, Any]) -> str:
    """
     Функция для отображения подучених аргов от другой функции в теримнале при логировании.
    :param keyword_args: словарь кваргов
    :return: строковое представление кваргов
    """
    if keyword_args:
        kwargs_list = [f"{key}={value}" for key, value in keyword_args.items()]
        kwars_str = ", ".join(kwargs_list) if len(kwargs_list) > 1 else kwargs_list[0]
        return kwars_str
    return ""


def _log_rich(renderable: Any, level: str = "INFO") -> None:
    """Записывает объект Rich в лог."""

    buffer = StringIO()

    console = Console(
        file=buffer,
        color_system=None,
        force_terminal=False,
    )

    console.print(renderable)

    logger.log(level, f"\n{buffer.getvalue()}")
