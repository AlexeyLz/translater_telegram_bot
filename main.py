import os
from bot_connection import dp
import bot_commands
from aiogram.utils import executor

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
