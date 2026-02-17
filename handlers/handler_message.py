# handlers/handler_message.py
import time
from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from wallett.kbds import inlinebtn  # убедитесь, что путь верный почему то ошибка в IDE
from utils import is_admin
import os
from wallett.googleteable import *
from datetime import datetime, timedelta
from wallett.logi import logi
from wallett.states import UserData  # ← Чистый и понятный импорт
from wallett.pydant import pydantic_models
from wallett.iiqwen import *

handler_message_router = Router()


@handler_message_router.message(F.text == "terminator")
async def reply_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ терминатора"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # ВСЯ ОСНОВНАЯ ЛОГИКА ТУТ
            logi.inf.info(f"проверка логи . ID - {message.from_user.id}")
            await message.answer("Данные о работе terminator", reply_markup=inlinebtn.terminator_variety())
    except Exception as e:
        logi.err.info(f"F.text == terminator в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(F.text == "⚡молния⚡")
async def light_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ молния"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # ВСЯ ОСНОВНАЯ ЛОГИКА ТУТ
            await message.answer("Данные о работе ⚡молния⚡", reply_markup=inlinebtn.lightning())
    except Exception as e:
        logi.err.info(f"light_btn() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------НАЧАЛО СОСТОЯНИЯ МОЛНИЯ--------------------------
# Команда /m — переключаемся в состояние для таблицы 1
# входим в состояние
@handler_message_router.message(F.text == "/m")
async def cmd_m(message: Message, state: FSMContext):
    """СОСТОЯНИЕ /m ВНОСИМ ДАННЫЕ В молнию"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer(f"работа с таблицей ⚡⚡⚡ молния ⚡⚡⚡")
        await state.set_state(UserData.TABLE_1)  # 🔑 Запоминаем контекст
        await message.answer("✏️ Введите данные для таблицы : SBER;b or s;12;309,34;вывод", parse_mode="HTML")
    except Exception as e:
        logi.err.info(f"cmd_m() в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(UserData.TABLE_1)
async def handle_table1_data(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return
        text = message.text.strip()
        # Парсим данные (разделяем по ;)
        parts = text.split(";", 4)  # Разбиваем на 5 части максимум
        if len(parts) != 5:
            await message.answer("Неверный формат!")
            return
        tiker, action, quantity, price, conclusion = parts
        d_light = pydantic_models.Lightning(tiker=tiker, action=action, quantity=quantity, price=price,
                                            conclusion=conclusion)
        now = datetime.now()
        # Форматированная дата "д.м.г"
        date_str = now.strftime("%Y-%m-%d")
        if d_light.action == "покупка":
            stop_market = round(d_light.price * 0.994, 2)
            stop_market_0 = round(d_light.price * 1.001, 2)
            take_profit = round(d_light.price * 1.03, 2)
        elif d_light.action == "продажа":
            stop_market = round(d_light.price * 1.006, 2)
            stop_market_0 = round(d_light.price * 0.999, 2)
            take_profit = round(d_light.price * 0.97, 2)
        else:
            logi.inf.info(
                f"handle_table1_data() в папке handlers/handler_message.py , не правильно написано {d_light.action}")
        plan_deistvi = [
            [d_light.tiker, "молния", d_light.action, date_str, d_light.quantity, d_light.price, stop_market,
             stop_market_0, take_profit, d_light.conclusion]]
        Dobavlenie(Nazvanie_operazii="", diapozon_dannich="молния!A5", znachenie=plan_deistvi, )
        await message.answer(f"🛑 Стоп маркет - {stop_market}")
        await message.answer(f"↔️ Безубыточность - {stop_market_0}")
        await message.answer(f"✅ Тейк-профит - {take_profit}")
        await message.answer(f"Данные сохранены в молния")
        await state.clear()  # Выходим из состояния
    except Exception as e:
        logi.err.info(f"handle_table1_data() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ СОСТОЯНИЯ МОЛНИЯ------------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ ДДС-------------------------

# Константы для бизнес-логики (выносим "магические числа")
MONTHLY_EXPENSES = 77_000  # ежемесячные расходы ???
CRITICAL_CASH_GAP = -5_000  # критический кассовый разрыв
# Маппинг месяца → буква столбца в Google Таблице (январь = B, февраль = C, ...)
MONTH_TO_COLUMN = {1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M"}
@handler_message_router.message(F.text == "ДДС")
async def dds_btn(message: types.Message):
    """ДДС вся логика и ответ на вопросы"""
    if not is_admin(message.from_user.id):
        await message.delete()
        return
    # Определяем текущий месяц и букву столбца
    month = datetime.now().month
    column = MONTH_TO_COLUMN.get(month)
    if not column:
        await message.answer("Ошибка: неизвестный месяц (должно быть 1-12)")
        logi.err.info(f"dds_btn() неизвестный месяц handlers/handler_message.py ")
        return
    # Читаем данные из таблицы
    try:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}3")[0]
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}18")[0]
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}59")[0]
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}58")[0]
    except Exception as e:
        logi.err.info(f"dds_btn() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}")
        return

    # -----------------------------------------------------------
    # 💰 Формируем ответ (используем f-строки для читаемости)
    months_covered = round(int(dds_ostatok) / MONTHLY_EXPENSES, 1)
    await message.answer(
        "📊 ФИНАНСОВЫЙ ОТЧЁТ ПО ДДС\n\n"
        f"Входящий поток: {dds_vchod} ₽\n"
        f"Исходящий поток: {dds_izchod} ₽\n"
        f"Остаток на руках: {dds_ostatok} ₽\n"
        f"Хватит на: {months_covered} мес.\n"
        f"Кассовый разрыв: {dds_kassa} ₽")

    # ⚠️ Анализ кассового разрыва
    cash_gap = int(dds_kassa)

    if cash_gap < CRITICAL_CASH_GAP:
        cushion_needed = abs(cash_gap) * 3
        await message.answer(
            "🔴 КРИТИЧЕСКИЙ КАССОВЫЙ РАЗРЫВ!\n"
            "Срочные меры:\n"
            "1️⃣ Товар копится на складе — проанализировать продажи\n"
            "2️⃣ Много сезонного товара — уменьшить закупки + распродажа\n"
            "3️⃣ Ошибки в бюджете — пересмотреть приоритеты\n"
            f"4️⃣ Нужна финансовая подушка: {cushion_needed:,} ₽\n"
            "5️⃣ Где можно сэкономить?\n"
            "6️⃣ Кто перестал платить и почему?\n"
            "☠️ ЭТО ПРЕДЕЛ!"
        )
    elif cash_gap < 0:
        cushion_needed = abs(cash_gap) * 3
        await message.answer(
            "🟡 КАССОВЫЙ РАЗРЫВ!\n"
            "Баланс расходов/доходов нарушен.\n"
            "Срочно принимайте меры!\n"
            f"Рекомендуемая подушка: {cushion_needed:,} ₽\n"
            "🫵"
        )
    else:
        await message.answer(
            "🟢 КАССОВЫЙ РАЗРЫВ ОТСУТСТВУЕТ!\n"
            "Все платежи покрыты.\n"
            "👍"
        )


#   ----------------КОНЕЦ СОСТОЯНИЯ ДДС-------------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ ДЕЛА-----------------------
@handler_message_router.message(F.text == "ДЕЛА")
async def do_list(message: types.Message):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer(f"Здесь рандомно показываются дела")
    except Exception as e:
        logi.err.info(f"do_list() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ СОСТОЯНИЯ ДЕЛА------------------------

#   ----------------НАЧАЛО СОСТОЯНИЯ МЕНЕДЖМЕНТ-----------------
@handler_message_router.message()
async def management(message: types.Message):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer(f"работа с таблицей 💸Дела и управление💸")
        # Форматированная дата "д.м.г"
        date_str = datetime.now().strftime("%Y-%m-%d")
        text = pydantic_models.StartIndication(text=message.text.strip())
        intellig = intelligence_def(text=text.text, client=client)
        intelligence = pydantic_models.StartIndication(text=intellig)
        await message.answer(intelligence.text)
        action_plan = [["zzz", date_str, "zzz", "zzz", text.text, intelligence.text, "zzz", "С+А", "zzz", "zzz", ]]
        Dobavlenie_vstavka_strok(Nazvanie_operazii="", diapozon_dannich="Дела и управление!A5", znachenie=action_plan, )
        await message.answer("👍")
        await message.answer("ОТЛИЧНАЯ ИДЕЯ!Спасибо ХОЗЯИН", reply_markup=inlinebtn.management_btn())
    except Exception as e:
        logi.err.info(f"management() в папке handlers/handler_message.py , Exception as e : {e}")

#   ----------------КОНЕЦ СОСТОЯНИЯ МЕНЕДЖМЕНТ--------------------------
