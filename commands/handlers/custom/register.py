"""Регистрация пользователя"""
from commands.decorators import command
from keyboards import get_yes_no_menu
from vk_bot import MessageContext


@command(["регистрация"])
def register_command(context: MessageContext):
    """Запуск регистрации пользователя"""
    user_name = context.bot.get_user_name(user_id=context.user_id)

    message = (f"Я посмотрел ваше имя в профиле в вк.\n"
               f"'{user_name}' ваше настоящее имя или указать другое?")

    return message, get_yes_no_menu()


# Todo сделать все этапы регистрации без бд
"""1) Написать - 
   Я посмотрел ваше имя в профиле в вк.
   Это ваше настоящее имя или указать другое?
   
   -Если ввели да то сохранить данные, если нет, то запросит данные и сохранить
   Данные на запрос: имя, фамилия, номер телеофна
   
   2) Сохранить данные в бд """
