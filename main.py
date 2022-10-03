import os
from bot_connection import dp
import bot_commands
from aiogram import types
from aiogram.utils import executor
import logging
from bot_connection import TOKEN, bot
APP_NAME = os.getenv('APP_NAME')
from aiogram.utils.executor import start_webhook

WEBHOOK_HOST = 'https://tranlate-boy.onrender.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '52.59.103.54'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
