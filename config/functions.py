from aiogram.utils.keyboard import InlineKeyboardBuilder

from .config import (
    bot, weblink, youtubelink, 
    time_interval, time_interval_sec, time_start,
    logger
)
from .text import *

import asyncio
import datetime


date_now = {}
date_now2 = {}

check_list = []
task = [] 



async def make_button(button_data):
    try:
        keyboardmain = InlineKeyboardBuilder()

        for text, callback_data in button_data:
            if 'http' in callback_data:
                keyboardmain.button(text=text, url=callback_data)
            elif 'Подарить счастье друзьям' in text:
                keyboardmain.button(text=text, switch_inline_query=callback_data)
            else:
                keyboardmain.button(text=text, callback_data=callback_data)

        # Создаем InlineKeyboardMarkup из списка кнопок
        keyboardmain.adjust(3)

        return keyboardmain.as_markup()
    except Exception as e:
        logger.critical(f'Error in "make_button": {e}')
    


""" =============================== сообщения отправляющиеся циклично =============================== """
async def m1(user_id):
    try:
        await bot.send_message(user_id, mes1, 
                            reply_markup=None)  
    except Exception as e:
        logger.critical(f'Error in "m1": {e}')

async def m2(user_id):
    try:
        await bot.send_message(user_id, mes2, 
                            reply_markup=await make_button([(
                                'ПЕРЕЙТИ', weblink
                            )]))  
    except Exception as e:
        logger.critical(f'Error in "m2": {e}')

async def m3(user_id):
    try:
        await bot.send_message(user_id, mes3, 
                            reply_markup=await make_button([(
                                'You-Tube', youtubelink
                            )])) 
    except Exception as e:
        logger.critical(f'Error in "m3": {e}')


async def m4(user_id):
    try:
        await bot.send_message(user_id, mes4, 
                            reply_markup=None) 
    except Exception as e:
        logger.critical(f'Error in "m4": {e}')

async def m5(user_id):
    try:
        await bot.send_message(user_id, mes5, 
 
                            reply_markup=await make_button([(
                                'ПЕРЕЙТИ', weblink
                            )]))
    except Exception as e:
        logger.critical(f'Error in "m5": {e}')

async def m6(user_id):
    try:
        await bot.send_message(user_id, mes6,  
                            reply_markup=await make_button([(
                                'ПЕРЕЙТИ', weblink
                            )]))
    except Exception as e:
        logger.critical(f'Error in "m6": {e}')

async def m7(user_id):
    try:
        await bot.send_message(user_id, mes7, 
 
                            reply_markup=await make_button([(
                                'ПЕРЕЙТИ', weblink
                            )]))
    except Exception as e:
        logger.critical(f'Error in "m7": {e}')
    


async def send_periodic_message1(user_id, var): 
    try:
        logger.info('В начале функции')
        current_time = datetime.datetime.now().time()
        logger.info(current_time)

        start_time = datetime.time(8, 0)  # Устанавливаем начальное время
        end_time = datetime.time(22, 0)  # Устанавливаем конечное время

        
        await asyncio.sleep(time_start)
    except Exception as e:
        logger.critical(f'Error in "send_periodic_message1": {e}')
    
    try:
        logger.info(f'var: {var}')
        while True:
            if start_time <= datetime.datetime.now().time() <= end_time:
                logger.info(f'NOW1: {datetime.datetime.now().time()}')
                try:
                    if not f'1mes{user_id}' in check_list:

                        date_now[user_id] = datetime.datetime.now()
                        date_now2[user_id] = datetime.datetime.now()

                        await m1(user_id)

                        check_list.append(f'1mes{user_id}')

                        logger.info(f'check_list: {check_list}')
                        logger.info('Отправили 1')
                        logger.info(f'Словарь дат 1: {date_now}')

                        await asyncio.sleep(time_interval_sec)


                    if not f'2mes{user_id}' in check_list:
                        if datetime.datetime.now() > date_now[user_id] + datetime.timedelta(hours=24):

                            await m2(user_id)

                            check_list.append(f'2mes{user_id}')

                            logger.info(f'check_list: {check_list}')
                            logger.info('Отправили 2')
                            logger.info(f'Словарь дат 2: {date_now}')

                            await asyncio.sleep(time_interval_sec)


                    if not f'3mes{user_id}' in check_list:
                        if datetime.datetime.now() > date_now[user_id] + datetime.timedelta(hours=48):

                            await m3(user_id)

                            check_list.append(f'3mes{user_id}')

                            logger.info(f'check_list: {check_list}')
                            logger.info('Отправили 3')
                            logger.info(f'Словарь дат 3: {date_now}')

                            await asyncio.sleep(time_interval_sec)


                    if not f'4mes{user_id}' in check_list:
                        if datetime.datetime.now() > date_now[user_id] + datetime.timedelta(hours=72):

                            await m4(user_id)

                            check_list.append(f'4mes{user_id}')

                            logger.info(f'check_list: {check_list}')
                            logger.info('Отправили 4')
                            logger.info(f'Словарь дат 4: {date_now}')

                            logger.info(f'Словарь дат 4: {date_now}')
                            await asyncio.sleep(time_interval_sec)

                    if not f'5mes{user_id}' in check_list:
                        if datetime.datetime.now() > date_now[user_id] + datetime.timedelta(hours=96):

                            await m5(user_id)

                            check_list.append(f'5mes{user_id}')

                            logger.info(f'check_list: {check_list}')
                            logger.info('Отправили 5')
                            logger.info(f'Словарь дат 5: {date_now}')

                            logger.info(f'Словарь дат 5: {date_now}')
                            await asyncio.sleep(time_interval_sec)

                    logger.info(f'Словарь дат перед очисткой!Before: {date_now}')
                    logger.info(f'Список перед очисткой!Before: {check_list}')


                    if datetime.datetime.now() > date_now[user_id] + datetime.timedelta(hours=119):

                        del date_now[user_id]

                        check_list.remove(f'1mes{user_id}')
                        check_list.remove(f'2mes{user_id}')
                        check_list.remove(f'3mes{user_id}')
                        check_list.remove(f'4mes{user_id}')
                        check_list.remove(f'5mes{user_id}')

                        logger.info('Очистили')

                        await asyncio.sleep(time_interval_sec)

                        logger.info(f'Словарь дат после очисткой!After: {date_now}')
                        logger.info(f'Список после очисткой!After: {check_list}')

                except Exception as e:
                    logger.critical(f'Ошибка в цикле 1: {e}')

                logger.info(f'check_list в конце цикла: {check_list}')
                logger.info(f'Словарь дат finish: {date_now}')
                
                await asyncio.sleep(time_interval)

            else:
                logger.info('Ночь')
                logger.info(f'Ночь: {current_time}')

            await asyncio.sleep(time_interval)

    except Exception as e:
        logger.critical(f'Ошибка в запуске отправки сообщений 1: {e}')
    

async def send_periodic_message2(user_id, var): 

    try:
        logger.info('В начале функции')
        current_time = datetime.datetime.now().time()
        current_date = datetime.datetime.now()
        # current_date = datetime.datetime(2023, 11, 29, 19, 0) # test
        start_time = datetime.time(7, 0)  # Устанавливаем начальное время
        end_time = datetime.time(22, 0)  # Устанавливаем конечное время

        
        await asyncio.sleep(time_start)
    except Exception as e:
        logger.critical(f'Error in "send_periodic_message2": {e}')
    
    logger.info('Попали в это место')
    
    try:
        logger.info(f'var: {var}')
        while True:
            if start_time <= datetime.datetime.now().time() <= end_time:

                if not f'6mes{user_id}' in check_list:
                    if datetime.datetime.now() > date_now2[user_id] + datetime.timedelta(hours=24*14):

                        await m6(user_id)

                        check_list.append(f'6mes{user_id}')

                        logger.info(f'check_list: {check_list}')
                        logger.info('Отправили 6')
                        logger.info(f'Словарь дат 6: {date_now2}')

                        logger.info(f'Словарь дат 6: {date_now2}')
                        await asyncio.sleep(time_interval_sec)


                if not f'7mes{user_id}' in check_list:
                    if datetime.datetime.now() > date_now2[user_id] + datetime.timedelta(hours=24*30):
                        
                        await m7(user_id)

                        check_list.append(f'7mes{user_id}')

                        logger.info(f'check_list: {check_list}')
                        logger.info('Отправили 7')
                        logger.info(f'Словарь дат 7: {date_now2}')

                        logger.info(f'Словарь дат 7: {date_now2}')
                        await asyncio.sleep(time_interval_sec)
                
                logger.info(f'Словарь дат перед очисткой!Before: {date_now2}')
                logger.info(f'Список перед очисткой!Before: {check_list}')


                if datetime.datetime.now() > date_now2[user_id] + datetime.timedelta(hours=24*30+2):

                    del date_now2[user_id]

                    check_list.remove(f'6mes{user_id}')
                    check_list.remove(f'7mes{user_id}')

                    logger.info('Очистили')

                    await asyncio.sleep(time_interval_sec)

                    logger.info(f'Словарь дат после очисткой!After: {date_now}')
                    logger.info(f'Список после очисткой!After: {check_list}')
            else:
                logger.info('Ночь2')

            await asyncio.sleep(time_interval)

    except Exception as e:
        logger.critical(f'Ошибка в запуске отправки сообщений 2: {e}')