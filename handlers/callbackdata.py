# handlers/callbackdata.py

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext  # если понадобится состояние
from wallett.kbds.inlinebtn import terminator_variety, lightning  # явный импорт нужных функций
from utils import is_admin
from wallett.logi import logi

callback_router = Router()


# ---------------------НАЧАЛО КНОПОК ДЛЯ молнии-----------------
@callback_router.callback_query(F.data == "result_day")
async def process_result_day(callback: CallbackQuery, state: FSMContext):
    """РЕЗУЛЬТАТЫ ЗА ДЕНЬ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю данные за день...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_day() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "result_month")
async def process_result_month(callback: CallbackQuery, state: FSMContext):
    """РЕЗУЛЬТАТЫ ЗА МЕСЯЦ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю данные за месяц...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_month() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "win_rate")
async def process_result_win_rate(callback: CallbackQuery, state: FSMContext):
    """win_rate"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю win_rate...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_win_rate() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "rez1")
async def process_result_rez1(callback: CallbackQuery, state: FSMContext):
    """rez1"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю rez1...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_rez1() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "rez2")
async def process_result_rez2(callback: CallbackQuery, state: FSMContext):
    """rez2"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю данные за rez2...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_rez2() в папке handlers/callbackdata , Exception as e : {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ молнии-----------------


# ---------------------НАЧАЛО КНОПОК ДЛЯ terminator-----------------
@callback_router.callback_query(F.data == "result_day_terminator")
async def result_day_terminator_def(callback: CallbackQuery, state: FSMContext):
    """РЕЗУЛЬТАТЫ ЗА ДЕНЬ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("terminator за день...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"result_day_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "result_month_terminator")
async def result_month_terminator_def(callback: CallbackQuery, state: FSMContext):
    """РЕЗУЛЬТАТЫ ЗА МЕСЯЦ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("terminator за месяц...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"result_month_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "win_rate_terminator")
async def win_rate_terminator_def(callback: CallbackQuery, state: FSMContext):
    """win_rate"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю win_rate...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"win_rate_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "briefcase")
async def briefcase_def(callback: CallbackQuery, state: FSMContext):
    """ЧТО В ПОРТФЕЛЕ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("ЧТО В ПОРТФЕЛЕ...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"briefcase_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "rez_terminator")
async def process_result_rez_terminator(callback: CallbackQuery, state: FSMContext):
    """rez_terminator"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("rez_terminator...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_result_rez_terminator() в папке handlers/callbackdata , Exception as e : {e}")
# ---------------------КОНЕЦ КНОПОК ДЛЯ terminator-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ УПРАВЛЕНИЕ-----------------
@callback_router.callback_query(F.data == "random")
async def process_management(callback: CallbackQuery, state: FSMContext):
    """РАНДОМНО ВЫДАЕТ ЗАДАЧИ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("random...", show_alert=False)
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"process_management() в папке handlers/callbackdata , Exception as e : {e}")
# ---------------------КОНЕЦ КНОПОК ДЛЯ УПРАВЛЕНИЕ-----------------
