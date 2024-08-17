import asyncio

from aiogram import Bot, Dispatcher
from handlers import router

from constants import token


async def start_tg() -> None:
    """Entry point"""
    while True:
        bot = Bot(token)
        dp = Dispatcher()
        dp.include_router(router)
        try:
            await bot.delete_webhook(drop_pending_updates=True)
            await dp.start_polling(bot)
        except Exception as _exx:
            print(f"start_tg - error: {_exx}")


print("voice bot started")
if __name__ == '__main__':
    try:
        asyncio.run(start_tg())
    except Exception as _ex:
        print(f"entry error: {_ex}")
