from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
import asyncio
from googleteable import *
from handlers.start import router as start_router
from handlers.handler_message import handler_message_router as h_m_router
from handlers import callbackdata
from logi import logi

# Загружаем .env только если файл существует (локально)
if os.path.exists(".env.wallet"):
    load_dotenv(".env.wallet")

# 📦 Прокси настройки (добавьте в .env)
# PROXY_URL=http://user:password@proxy_ip:port
PROXY_URL = os.getenv("PROXY_URL")  # например: "http://login:pass@123.45.67.89:8080"

# Создаём сессию с прокси
session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else AiohttpSession()

bot = Bot(os.getenv("TOKEN"), session=session)  # ← передаём session
dp = Dispatcher()
my_admins_list = os.getenv("my_admins")
my_admins_list_2 = os.getenv("my_admins2")


async def main():
    dp.include_router(start_router)
    dp.include_router(h_m_router)
    dp.include_router(callbackdata.callback_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # После получения PROXY_URL из env
    if PROXY_URL := os.getenv("PROXY_URL"):
        from urllib.parse import urlparse, unquote

        p = urlparse(PROXY_URL)
        login = f"{unquote(p.username)[:2]}****:" if p.username else ""
        print(f"🌐 Прокси: {p.scheme.upper()}://{login}****@{p.hostname}:{p.port}")
    else:
        print("🌐 Прокси: ❌ не задан ttt")

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logi.err.info("РОБОТ gnom sem87sem это яяяяяяяяя ОСТАНОВЛЕН В РУЧНУЮ")
    except Exception as e:
        logi.err.info(f"main , Exception as e : {e}")
