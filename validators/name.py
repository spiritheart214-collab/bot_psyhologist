"""Валидаторы ввода имени и фамилии."""
import re


def _check_name(name: str) -> bool:
    """
    Проверяет корректность имени.

    :param name: Имя пользователя
    :return: True/False
    """
    name = name.strip()

    if not name:
        return False

    if len(name) < 2 or len(name) > 30:
        return False

    pattern = r"^[А-Яа-яЁёA-Za-z]+(?:-[А-Яа-яЁёA-Za-z]+)*$"

    return bool(re.fullmatch(pattern, name))


def validate_name(name: str) -> str | None:
    """
    Проверяет и форматирует имя.

    :param name: Имя пользователя
    :return: Отформатированное имя или None
    """
    if not _check_name(name):
        return None

    name = name.strip()
    return "-".join(part.capitalize() for part in name.split("-"))


def _check_surname(surname: str) -> bool:
    """
    Проверяет корректность фамилии.

    :param surname: Фамилия пользователя
    :return: True/False
    """
    surname = surname.strip()

    if not surname:
        return False

    if len(surname) < 2 or len(surname) > 30:
        return False

    pattern = r"^[А-Яа-яЁёA-Za-z]+(?:-[А-Яа-яЁёA-Za-z]+)*$"

    return bool(re.fullmatch(pattern, surname))


def validate_surname(surname: str) -> str | None:
    """
    Проверяет и форматирует фамилию.

    :param surname: Фамилия пользователя
    :return: Отформатированная фамилия или None
    """
    if not _check_surname(surname):
        return None

    surname = surname.strip()
    return "-".join(part.capitalize() for part in surname.split("-"))