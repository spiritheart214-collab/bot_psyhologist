"""Основной файл приложения"""
from vk_api.longpoll import VkEventType

from commands import get_command, handle_active
from logger import logger
from vk_bot import VKBot, MessageContext


def main():
    """Запуск бота. Основная программная функция"""
    vk_bot = VKBot()

    logger.success("Бот запущен!")

    # Перебираем все события
    for event in vk_bot.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            context = MessageContext(user_id=event.user_id, text=event.text.lower().strip(), bot=vk_bot)

            # Todo рассмотреть возможность выввести это в диспатчер создав функцию handle_message , где будет \
            #  handle_active get_command(context=context) и  vk_bot.send_message. Чтобы все собрать в одном месте

            # Если пользователь находится в каком-то состоянии
            if handle_active(context=context):
                # Очень важно: Если состояние было найдено, дальше get_command() не вызываем.
                continue

            message, keyboard = get_command(context=context)
            vk_bot.send_message(user_id=context.user_id, message=message, keyboard=keyboard)


if __name__ == '__main__':
    main()
