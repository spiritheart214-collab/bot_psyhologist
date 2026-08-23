"""Основной файл приложения"""
from vk_api.longpoll import VkEventType

from commands import handle_massage
from logger import logger
from vk_bot import VKBot, MessageContext


def main():
    """Запуск бота. Основная программная функция"""
    vk_bot = VKBot()
    logger.success("Бот запущен!")

    for event in vk_bot.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            context = MessageContext(user_id=event.user_id, text=event.text.lower().strip(), bot=vk_bot)
            handle_massage(context)


if __name__ == '__main__':
    main()
