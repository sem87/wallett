# handlers/start.py
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from wallett.kbds.reply import start_kb
from wallett.logi import logi
from utils import is_admin
import os

router = Router()  # ← создаём роутер


@router.message(CommandStart())
async def start_cmd(message: Message):
    """УЗНАЕМ ПРАВА ДОСТУПА"""
    try:
        if not is_admin(message.from_user.id):
            logi.err.info(f"ВНИМАНИЕ!!! НЕСАНКЦИОНИРОВАННОЕ ПРОНИКНОВЕНИЕ - {message.from_user.id}")
            await message.delete()
            return
        else:
            await message.answer("ПРИВЕТ!!! Я КОШЕЛЕК", reply_markup=start_kb)
    except Exception as e:
        logi.err.info(f"start_cmd в папке handlers/start.py , Exception as e : {e}")
