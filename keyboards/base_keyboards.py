"""Модуль с базовыми клавиатурами для бота"""
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_register_menu() -> str:
    """
    Главное меню для неавтаризованного пользоватля. С 2-мя кнопками:
        1) Регистрация
        2) Помощь
    """

    keyboard = VkKeyboard()

    keyboard.add_button("Регистрация", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Помощь", color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()


def get_yes_no_menu() -> str:
    """ Да / Нет клавиатура"""

    keyboard = VkKeyboard(inline=True)

    keyboard.add_button("Да", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Нет", color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()
