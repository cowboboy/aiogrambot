from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/help")
b2 = KeyboardButton("/menu")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2)