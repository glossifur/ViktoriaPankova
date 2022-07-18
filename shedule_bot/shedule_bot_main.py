import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import logging
import os
from shedule_bot.config import schedule
from shedule_bot.buttons import user_kb


bot = Bot('5476961966:AAHlZYaYxuPzZzwGGqbLfauD_csMNII-Djg')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}, я бот,который может '
                               f'подсказать расписание уроков', reply_markup=user_kb)


@dp.message_handler(Text(equals=schedule.keys(), ignore_case=True))
async def get_all_schedule(message: types.Message):
    msg = schedule[message.text]
    await bot.send_message(message.from_user.id, f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals='Сегодня', ignore_case=True))
async def get_schedule(message: types.Message):
    msg = schedule[
        list(schedule.keys())[datetime.datetime.now().weekday()]
    ]
    await bot.send_message(message.from_user.id, f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)

    @dp.message_handler(Text(equals='Завтра', ignore_case=True))
    async def get_schedule_tommorow(message: types.Message):
        msg = schedule[
            list(schedule.keys())[datetime.datetime.now().weekday() + 1]
        ]
        await bot.send_message(message.from_user.id, f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)
