from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import logging

TOKEN = '#'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

weblink = 'https://happy1.ru/practical_happiness' # ссылка на сайт
youtubelink = 'https://www.youtube.com/@_happy1.ru_' # cсылка на ютуб


time_start = 10
time_interval = 60 * 5 # каждые 5 минуты обновление
time_interval_sec = 10
time_interval_for_site = 3600 * 12


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)