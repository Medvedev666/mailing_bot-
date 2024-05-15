from aiogram import Dispatcher 
from aiogram.filters import CommandStart

import asyncio
import logging
import sys

from config.config import bot, logger
from config.functions import (
    make_button,
    task, send_periodic_message1, send_periodic_message2
)
from config.list import button_list

dp = Dispatcher() 


command_queue = asyncio.Queue()


#=========================

@dp.message(CommandStart())
async def welcome(message):
    try:
        # Отправляем приветственное сообщение с клавиатурой
        await message.answer(f'Здравствуйте, на связи Александр Пискулин и я рад приветствовать вас в мире '
                                'счастьеведения \n'
                                '<b>«Про Счастье, как смысл жизни»</b>.', 
                            reply_markup=await make_button(button_list))
        user_id = message.from_user.id 
        var = True
        if not user_id in task:

            logger.info(f'Task list: {task}')
            asyncio.create_task(send_periodic_message1(user_id, var))
            asyncio.create_task(send_periodic_message2(user_id, var))
            task.append(user_id)
    except Exception as e:
        logger.info(f'Error in "welcome": {e}')


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())