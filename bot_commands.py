import asyncio

from bot_connection import dp
import os
from bot_connection import dp
import bot_texts as texts
import translate_by_google as google_trans
import info_word
import bot_commands
import keyboards
from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.utils import executor


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет ' + str(message.from_user.first_name) + '!\n' + texts.start_text)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(texts.help_text)


@dp.message_handler(commands=['translate'])
async def echo(message: types.Message):
    arguments = message.get_args()
    if arguments == '' or arguments == ' ':
        await message.answer('Вы не ввели текст для перевода')
        return
    msg = await message.answer('Перевожу...')
    text = google_trans.translate(arguments)

    await msg.edit_text(text)


@dp.message_handler(commands=['info'])
async def echo(message: types.Message):
    arguments = message.get_args()
    if arguments == '' or arguments == ' ':
        await message.answer('Вы не ввели слово для получения информации')
        return
    msg = await message.answer('Поиск информации... о ' + arguments)
    answer = info_word.info(arguments)
    if not answer:
        await msg.edit_text('Ничего не найдено по запросу')
        return

    await message.answer(texts.info_word_text, reply_markup=keyboards.get_keyboard_info_word(answer, arguments))


@dp.callback_query_handler(Text(startswith="info_word_state"))
async def callbacks_num(call: types.CallbackQuery):
    word_data = call.data.split("_")[3]
    word_result = call.data.split("_")[4]
    await call.message.delete()
    print(word_result, word_data)

    await call.message.answer('Информация о ' + word_result + ':\n'+info_word.get_info_word(word_data, word_result))
