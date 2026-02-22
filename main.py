from aiogram import Bot, Dispatcher
import asyncio
from googleteable import *
from handlers.start import router as start_router
from handlers.handler_message import handler_message_router as h_m_router
from handlers import callbackdata
from wallett.logi import logi

load_dotenv(".env.wallet")
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()
my_admins_list = os.getenv("my_admins")
my_admins_list_2 = os.getenv("my_admins2")


async def main():
    dp.include_router(start_router)
    dp.include_router(h_m_router)
    dp.include_router(callbackdata.callback_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logi.err.info("РОБОТ ОСТАНОВЛЕН В РУЧНУЮ")
    except Exception as e:
        logi.err.info(f"main , Exception as e : {e}")

