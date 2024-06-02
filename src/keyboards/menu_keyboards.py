from typing import Optional

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config


INVITE_URL = f"https://t.me/{Config.bot_id}?startgroup=true"


def main_menu(condition: Optional = None):
    kb = [
        [InlineKeyboardButton(text='🗃️ My polls', callback_data='my_polls')],
        [InlineKeyboardButton(text='📆 Create Poll', callback_data='create_poll'), InlineKeyboardButton(text='🛑 Stop Poll', callback_data='stop_poll')],
        [InlineKeyboardButton(text='❔ How it works', callback_data='how_it_works'), InlineKeyboardButton(text='ℹ️ About', callback_data='about')]
    ]
    if condition == 'invite':
        kb.insert(0, [InlineKeyboardButton(text='➕ Invite to group', url=INVITE_URL)])
    keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=kb)
    return keyboard


