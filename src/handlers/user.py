from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


from src.keyboards import menu_keyboards as kb


router = Router()


@router.message(Command('start'))
async def start(m: Message):

    await m.answer(
        "Hello. I'm Football Gather Bot, here to help you organize and manage your football games effortlessly!\n"
        "What you would like to do?",
        reply_markup=kb.main_menu()
    )
