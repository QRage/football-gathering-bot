import asyncio

from aiogram import Bot, Dispatcher

from config import Config
from src.handlers import user


bot = Bot(token=Config.token)
dp = Dispatcher()


async def main():
    try:
        dp.include_router(user.router)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Exit init. Bot Stopped!')

