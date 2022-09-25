import os

from aiogram import Bot

from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
