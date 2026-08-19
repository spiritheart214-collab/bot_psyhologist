"""Основной файл приложения"""

from vk_api.longpoll import VkEventType

from vk_bot import VKBot
from logger import logger

from commands import get_command


def main():
    """Запуск бота. Основная программная функция"""
    vk_bot = VKBot()

    logger.success("Бот запущен!")

    # Перебираем все события
    for event in vk_bot.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            # Забираем данные пользователя
            user_id = event.user_id
            user_message = event.text.lower().strip()

            message, keyboard = get_command(name=user_message)
            vk_bot.send_message(user_id=user_id, message=message, keyboard=keyboard)


if __name__ == '__main__':
    main()
