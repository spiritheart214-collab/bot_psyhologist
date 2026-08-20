"""Основной файл приложения"""
from vk_api.longpoll import VkEventType

from commands import get_command
from logger import logger
from vk_bot import VKBot, MessageContext
from states import handle_state


def main():
    """Запуск бота. Основная программная функция"""
    vk_bot = VKBot()

    logger.success("Бот запущен!")

    # Перебираем все события
    for event in vk_bot.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            context = MessageContext(user_id=event.user_id, text=event.text.lower().strip(), bot=vk_bot)

            # Если пользователь находится в каком-то состоянии
            if handle_state(context=context):
                # Очень важно: Если состояние было найдено, дальше get_command() не вызываем.
                continue

            message, keyboard = get_command(context=context)
            vk_bot.send_message(user_id=context.user_id, message=message, keyboard=keyboard)


if __name__ == '__main__':
    main()
