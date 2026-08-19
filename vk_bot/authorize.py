from dataclasses import dataclass

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll
from vk_api.vk_api import VkApiMethod

from config import bot_config
from logger import logger


@dataclass(slots=True)
class VKBot:
    vk_session: VkApi = None
    vk: VkApiMethod = None
    longpoll: VkLongPoll = None

    def __post_init__(self) -> None:
        """Авторизация бота в сети"""
        logger.debug("Начало авторизации бота ...")

        self.vk_session: VkApi = VkApi(token=bot_config.VK_TOKEN)
        self.vk: VkApiMethod = self.vk_session.get_api()
        self.longpoll: VkLongPoll = VkLongPoll(self.vk_session)

        logger.info("Бот авторизирован и готов к запуску !")

    def send_message(self, user_id: int, message: str, keyboard: str = None) -> None:
        """Отправка сообщений"""
        self.vk.messages.send(
            user_id=user_id,
            message=message,
            random_id=0,
            keyboard=keyboard
        )

    def get_user_name(self, user_id: int) -> str:
        """Получить имя пользователя"""
        user = self.vk.users.get(user_ids=user_id)[0]
        return f"{user['first_name']} {user['last_name']}"

