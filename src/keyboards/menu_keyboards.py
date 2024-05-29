from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_manu():
    kb = [
        [KeyboardButton(text='🗃️ My polls')],
        [KeyboardButton(text='📆 Create Poll'), KeyboardButton(text='🛑 Stop Poll')],
        [KeyboardButton(text='❔ How it works'), KeyboardButton(text='ℹ️️ About')]
        ]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    return keyboard

