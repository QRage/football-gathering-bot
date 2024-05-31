from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    kb = [
        [InlineKeyboardButton(text='🗃️ My polls', callback_data='my_polls')],
        [InlineKeyboardButton(text='📆 Create Poll', callback_data='create_poll'), InlineKeyboardButton(text='🛑 Stop Poll', callback_data='stop_poll')],
        [InlineKeyboardButton(text='❔ How it works', callback_data='how_it_works'), InlineKeyboardButton(text='ℹ️ About', callback_data='about')]
    ]
    keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=kb)
    return keyboard


def choose_group():
    # Assuming you have a list of available groups with IDs
    groups = [
        {'id': 1, 'name': 'Group 1'},
        {'id': 2, 'name': 'Group 2'},
        {'id': 3, 'name': 'Group 3'}
    ]
    kb = [
        [InlineKeyboardButton(text=group['name'], callback_data=f'choose_group_{group["id"]}')]
        for group in groups
    ]
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)
    return keyboard
