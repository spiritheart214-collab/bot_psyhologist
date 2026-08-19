"""Основной файл приложения"""
from vk_api.longpoll import VkEventType

from commands import get_command
from logger import logger
from vk_bot import VKBot
from states import handle_state


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

            # Если пользователь находится в каком-то состоянии
            if handle_state(user_id=user_id, user_message=user_message, vk_bot=vk_bot):
                # Очень важно: Если состояние было найдено, дальше get_command() не вызываем.
                continue

            message, keyboard = get_command(name=user_message, user_id=user_id)
            vk_bot.send_message(user_id=user_id, message=message, keyboard=keyboard)


if __name__ == '__main__':
    main()
