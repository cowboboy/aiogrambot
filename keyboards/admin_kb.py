from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_load = KeyboardButton("/Загрузить")
button_delete = KeyboardButton("/Удалить")

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.row(button_load, button_delete)