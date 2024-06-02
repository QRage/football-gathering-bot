from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from src.keyboards import menu_keyboards as kb
from run import bot


router = Router()


@router.message(Command('start'))
async def start(m: Message):
    if m.chat.type == 'private':
        await m.answer(
            "Hello. I'm Football Gather Bot, here to help you organize and manage your football games effortlessly!\n"
            "What you would like to do?",
            reply_markup=kb.main_menu()
        )
    elif m.chat.type in ['group', 'supergroup']:
        pass


@router.callback_query(F.data == 'my_polls')
async def create_poll(callback: CallbackQuery):
    # TODO polls check
    await callback.message.edit_text(
        'No polls found.\n'
        'What you would like to do?',
        reply_markup=kb.main_menu())


@router.callback_query(F.data == 'create_poll')
async def create_poll(callback: CallbackQuery):
    # TODO common group check
    await callback.message.edit_text(
        'No common groups found.\n'
        'What you would like to do?',
        reply_markup=kb.main_menu('invite'))



