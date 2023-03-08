from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)