from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommand, BotCommandScopeDefault
import asyncio
import random
from datetime import datetime, timedelta
from dotenv import find_dotenv, load_dotenv

# _____не было
import logi
from aiogram.fsm.storage.memory import MemoryStorage  # или RedisStorage

# свои модули
from googleteable import *
from googleteable2table import *
# from kbds import inlinebtn, reply
# from handlers import start
from handlers.start import router as start_router
from handlers.handler_message import handler_message_router as h_m_router
from handlers import callbackdata


load_dotenv(".env.wallet")
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()
my_admins_list = os.getenv("my_admins")
my_admins_list_2 = os.getenv("my_admins2")
# month_dict = {1: "ЯНВАРЬ", 2: "ФЕВРАЛЬ", 3: "МАРТ", 4: "АПРЕЛЬ", 5: "МАЙ", 6: "ИЮНЬ", 7: "ИЮЛЬ", 8: "АВГУСТ",
#               9: "СЕНТЯБРЬ", 10: "ОКТЯБРЬ", 11: "НОЯБРЬ", 12: "ДЕКАБРЬ", }


# ____________________НАЧАЛО РАБОТЫ________________________
# async def set_commands(bot: Bot):
#     commands = [
#         BotCommand(command="start", description="Начало работы"),
#         BotCommand(command="molnia_tabl", description="Ввод в молнию"),
#     ]
#     # Явная установка для всех приватных чатов
#     await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

async def main():
    # await set_commands(bot)
    dp.include_router(start_router)
    dp.include_router(h_m_router)
    dp.include_router(callbackdata.callback_router)
    await dp.start_polling(bot)
    # что это такое
    # await bot.set_my_commands(commands=[], scope=types.BotCommandScopeAllPrivateChats())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
        # logger.info("🛑 Бот остановлен вручную")
    except Exception as e:
        pass
        # logger.exception(f"❌ Критическая ошибка: {e}")
