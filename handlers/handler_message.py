# handlers/handler_message.py
import random
from datetime import datetime

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from googleteable import MONTH_TO_COLUMN, Delete_row, Dobavlenie, Dobavlenie_vstavka_strok, Izmenenie, Read
from iiqwen import client, intelligence_def
from kbds import inlinebtn  # убедитесь, что путь верный почему то ошибка в IDE
from logi import logi
from pydant import pydantic_models
from states import UserData  # ← Чистый и понятный импорт
from utils import is_admin


# from databazesql import databaze_sql_term

handler_message_router = Router()


#   ----------------НАЧАЛО КОНСТАНТЫ И ФУНКЦИИ БИЗНЕС ЛОГИКИ-------------------------
dict_ticker_number={
    "ROSN": 2,
    "TATN": 3,
    "LKOH": 4,
    "NVTK": 5,
    "SMLT": 6,
    "PIKK": 7,
    "RUAL": 8,
    "GMKN": 9,
    "PLZL": 10,
    "VTBR": 11,
    "SBER": 12,
    "T": 13,
    "EUTR": 14,
    "IRAO": 15,
    "ОФЗ 26225": 16,
    "ОФЗ 26230": 17,
    "ОФЗ 26233": 18,
    "ОФЗ 26235": 19,
    "ОФЗ 26238": 20,
    "ОФЗ 26240": 21,
    "TPAY": 22,
    "CNY": 23,
    "TGLD": 24,
    "USD": 25
}

def average_monthly(type_activity=18):
    """РАСЧИТЫВАЕТ СРЕДНИЕ ЗА 12 МЕС ДДС_РАСХОДЫ=18,ДДС_ДОХОДЫ=3,PNL_РАСХОДЫ=62,PNL_ДОХОДЫ=52"""
    try:
        dds_expenses = 0
        quantity = 0
        for month in range(1, 13, 1):
            column = MONTH_TO_COLUMN.get(month)
            mont = float(Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}{type_activity}")[0])
            if mont == 0.0:
                quantity += 0
                dds_expenses += mont
            else:
                dds_expenses += mont
                quantity += 1
        average_month = int(round(dds_expenses / quantity, 0))
        return average_month
    except Exception as e:
        logi.err.info(f"average_monthly() ошибка СРЕД РАСХ handlers/handler_message.py , Exception as e : {e}")


def format_money(value) -> str:
    """Форматирует число с пробелами между тысячами: 1000000 -> 1 000 000"""
    value = float(value)
    return f"{value:,.0f}".replace(",", " ")


#   ----------------КОНЕЦ КОНСТАНТЫ И ФУНКЦИИ БИЗНЕС ЛОГИКИ-------------------------


@handler_message_router.message(F.text == "необх финансы")
async def necessary_finances_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ необходимых финансов"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # Определяем текущий месяц и букву столбца
            month = datetime.now().month
            column = MONTH_TO_COLUMN.get(month)
            if not column:
                await message.answer("Ошибка: неизвестный месяц (должно быть 1-12)")
                logi.err.info("dds_btn() неизвестный месяц handlers/handler_message.py ")
                return
            # Читаем данные из таблицы
            try:
                required_income = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}166")[0]
                required_consumption = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}167")[0]
            except Exception as e:
                logi.err.info(f"necessary_finances_btn() ошибка ДДС,PNL handlers/handler_message, Exception as e : {e}")
            await message.answer(
                f"💵Необход доход мес: {format_money(int(required_income))}p\n"
                f"💵Необход доход день: {format_money(round(int(required_income) / 30))}p\n"
                f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                f"❗Необход расход мес: {format_money(int(required_consumption))}p\n"
                f"❗Необход расход день: {format_money(round(int(required_consumption) / 30))}p\n"
            )
    except Exception as e:
        logi.err.info(f"F.text == необх финансы в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(F.text == "🦾terminator🦾")
async def reply_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ терминатора"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # ВСЯ ОСНОВНАЯ ЛОГИКА ТУТ
            await message.answer("Данные о работе terminator", reply_markup=inlinebtn.terminator_variety())
    except Exception as e:
        logi.err.info(f"F.text == terminator в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(F.text == "⚡молния⚡/m")
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


@handler_message_router.message(F.text == "💹основной💹/o")
async def basics_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ основной"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # ВСЯ ОСНОВНАЯ ЛОГИКА ТУТ
            await message.answer("Данные о работе 💹основной💹", reply_markup=inlinebtn.basic_btn())
    except Exception as e:
        logi.err.info(f"basics_btn() в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(F.text == "💼состав💼/c")
async def compound_btn(message: types.Message):
    """ВСЕ ПО ПОВОДУ основной"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        else:
            # ВСЯ ОСНОВНАЯ ЛОГИКА ТУТ
            # Читаем данные из таблицы
            ticker_compound = "None"
            action_compound = "None"
            sum_compound = "0"
            for i in range(2, 26):
                try:
                    ticker_compound = Read(Nazvanie_operazii="", range=f"analystrade!Z{i}")[0]
                    action_compound = Read(Nazvanie_operazii="", range=f"analystrade!AA{i}")[0]
                    sum_compound = Read(Nazvanie_operazii="", range=f"analystrade!AB{i}")[0]
                except Exception as e:
                    logi.err.info(
                        f"compound_btn_btn() ошибка состав портф handlers/handler_message, Exception as e : {e}"
                    )
                await message.answer(f"{i}){ticker_compound}: 💵{sum_compound}p == {action_compound}\n")
    except Exception as e:
        logi.err.info(f"compound_btn() в папке handlers/handler_message.py , Exception as e : {e}")


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
        await message.answer("работа с таблицей ⚡⚡⚡ молния ⚡⚡⚡")
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
        d_light = pydantic_models.Lightning(
            tiker=tiker, action=action, quantity=quantity, price=price, conclusion=conclusion
        )
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
                f"handle_table1_data() в папке handlers/handler_message.py , не правильно написано {d_light.action}"
            )
        plan_deistvi = [
            [
                d_light.tiker,
                "молния",
                d_light.action,
                date_str,
                d_light.quantity,
                d_light.price,
                stop_market,
                stop_market_0,
                take_profit,
                d_light.conclusion,
            ]
        ]
        Dobavlenie(
            Nazvanie_operazii="",
            diapozon_dannich="молния!A5",
            znachenie=plan_deistvi,
        )
        await message.answer(f"🛑 Стоп маркет - {stop_market}")
        await message.answer(f"↔️ Безубыточность - {stop_market_0}")
        await message.answer(f"✅ Тейк-профит - {take_profit}")
        await message.answer("Данные сохранены в молния")
        await state.clear()  # Выходим из состояния
    except Exception as e:
        logi.err.info(f"handle_table1_data() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ СОСТОЯНИЯ МОЛНИЯ-----------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ ОСНОВНОЙ--------------------
# Команда /o — переключаемся в состояние для таблицы 2
# входим в состояние
@handler_message_router.message(F.text == "/o")
async def cmd_o(message: Message, state: FSMContext):
    """СОСТОЯНИЕ /o ВНОСИМ ДАННЫЕ В ОСНОВНОЙ"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer("работа с таблицей 💹основной💹")
        await state.set_state(UserData.TABLE_2_TICKER)  # Запоминаем контекст
        await message.answer("Введи тикер", parse_mode="HTML")
        # await message.answer("✏️ Введите данные для ОСНОВНОЙ : SBER;12;309,34;на что мой расчет или надежда?тренд-(вниз),план-(после дивидендов...)", parse_mode="HTML")
    except Exception as e:
        logi.err.info(f"cmd_o() в папке handlers/handler_message.py , Exception as e : {e}")


# 2. Шаг 1: Получаем тикер
@handler_message_router.message(UserData.TABLE_2_TICKER)
async def process_ticker(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return
        # Проверка на отмену переделать для кнопки
        if message.text.strip().lower() in ["отмена", "cancel", "/cancel"]:
            await state.clear()
            await message.answer("❌ Операция отменена.")
            return
        # Нужно прогнать тикер через пайдентик
        tiker = message.text.strip().upper()
        # Запоминаем тикер в "память" состояния
        await state.update_data(tiker=tiker)
        # читаю из памяти
        data_tiker = await state.get_data()
        tiker2 = data_tiker.get("tiker")
        if tiker2 in dict_ticker_number:
            num_str = dict_ticker_number[tiker2]
            total_capital = Read(Nazvanie_operazii="", range=f"analystrade!AB{num_str}")[0]
            related_products = Read(Nazvanie_operazii="", range=f"analystrade!AI{num_str}")[0]
            operating_principle = Read(Nazvanie_operazii="", range=f"analystrade!AJ{num_str}")[0]
            level_price = Read(Nazvanie_operazii="", range=f"analystrade!AK{num_str}")[0]
        else:
            total_capital = "нету"
            related_products = "нету"
            operating_principle = "нету"
            level_price = "нету"
        print(tiker2,related_products,level_price,operating_principle,total_capital)
        await message.answer(f"Всего капитал : {total_capital}")
        await message.answer(f"Влияет : {related_products}")
        await message.answer(f"Принцип работы : {operating_principle}")
        await message.answer(f"Ценовые уровни и кол-во : {level_price}")
        # Переходим к следующему шагу
        await state.set_state(UserData.TABLE_2_QUANTITY)
        await message.answer(
            f"✅ Тикер <b>{tiker}</b> сохранен.\n"
            "✏️ <b>Шаг 2 из 4:</b> Введите <b>количество</b> лотов.",
            parse_mode="HTML"
        )
    except Exception as e:
        logi.err.info(f"process_ticker() Exception: {e}")


# 3. Шаг 2: Получаем количество
@handler_message_router.message(UserData.TABLE_2_QUANTITY)
async def process_quantity(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return

        if message.text.strip().lower() in ["отмена", "cancel", "/cancel"]:
            await state.clear()
            await message.answer("❌ Операция отменена.")
            return

        quantity = message.text.strip()
        await state.update_data(quantity=quantity)

        await state.set_state(UserData.TABLE_2_PRICE)
        await message.answer(
            f"✅ Количество: <b>{quantity}</b>.\n"
            "✏️ <b>Шаг 3 из 4:</b> Введите <b>цену</b> покупки (например, 309.34 или 309,34).",
            parse_mode="HTML"
        )
    except Exception as e:
        logi.err.info(f"process_quantity() Exception: {e}")


# 4. Шаг 3: Получаем цену
@handler_message_router.message(UserData.TABLE_2_PRICE)
async def process_price(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return

        if message.text.strip().lower() in ["отмена", "cancel", "/cancel"]:
            await state.clear()
            await message.answer("❌ Операция отменена.")
            return

        # Заменяем запятую на точку для корректного float
        price_str = message.text.strip().replace(",", ".")
        try:
            price_float = float(price_str)
        except ValueError:
            await message.answer("❌ Неверный формат цены. Введите число (например, 309.34). Попробуйте еще раз:")
            return  # Не меняем состояние, ждем правильный ввод

        await state.update_data(price=price_float)

        await state.set_state(UserData.TABLE_2_CONCLUSION)
        await message.answer(
            f"✅ Цена: <b>{price_str}</b>.\n"
            "✏️ <b>Шаг 4 из 4:</b> Введите <b>вывод</b> (на что ваш расчет?).",
            parse_mode="HTML"
        )
    except Exception as e:
        logi.err.info(f"process_price() Exception: {e}")


# 5. Шаг 4: Получаем вывод и запускаем вашу логику сохранения
@handler_message_router.message(UserData.TABLE_2_CONCLUSION)
async def process_conclusion(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return

        if message.text.strip().lower() in ["отмена", "cancel", "/cancel"]:
            await state.clear()
            await message.answer("❌ Операция отменена.")
            return

        conclusion = message.text.strip()

        # Достаем все ранее сохраненные данные из FSM
        data = await state.get_data()
        tiker = data.get("tiker")
        quantity = data.get("quantity")
        price = data.get("price")  # Уже во float

        # Создаем модель
        d_basic = pydantic_models.Lightning(
            tiker=tiker,
            action="покупка",
            quantity=quantity,
            price=price,
            conclusion=conclusion
        )

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")

        # Ваши расчеты
        stop_market_basic = round(d_basic.price * 0.994, 2)
        stop_market_0_basic = round(d_basic.price * 1.001, 2)
        take_profit_basic = round(d_basic.price * 1.03, 2)
        vivod_itog = "zzz"

        # Чтение из Google Таблиц
        tiker_to_dict = d_basic.tiker.upper()
        if tiker_to_dict in dict_ticker_number:
            i = dict_ticker_number[tiker_to_dict]
            related_products = Read(Nazvanie_operazii="", range=f"analystrade!AI{i}")[0]
            # Примечание: в вашем оригинальном коде level_price читался из той же ячейки AI.
            # Если нужна другая колонка, измените букву (например, AJ)
            level_price = Read(Nazvanie_operazii="", range=f"analystrade!AI{i}")[0]
        else:
            related_products = "нет такого тикера!"
            level_price = "нет данных по уровням"

        # Запись в Google Таблицы
        plan_deistvi_basic = [
            [d_basic.tiker, "основной", d_basic.action, date_str, d_basic.quantity, d_basic.price, d_basic.conclusion,
             vivod_itog, related_products]
        ]
        Dobavlenie(Nazvanie_operazii="", diapozon_dannich="основной!A5", znachenie=plan_deistvi_basic)

        # Отправка ответов пользователю
        await message.answer(f"🛑 Стоп маркет - {stop_market_basic}")
        await message.answer(f"↔️ Безубыточность - {stop_market_0_basic}")
        await message.answer(f"✅ Тейк-профит - {take_profit_basic}")
        await message.answer(f"Напоминаю: {level_price}")
        await message.answer("✅ Данные успешно сохранены в 💹основной💹")

        # Полностью очищаем состояние в самом конце
        await state.clear()

    except Exception as e:
        logi.err.info(f"process_conclusion() Exception: {e}")
        await state.clear()

# @handler_message_router.message(UserData.TABLE_2)
# async def handle_table2_data_basic(message: Message, state: FSMContext):
#     try:
#         if not is_admin(message.from_user.id):
#             await message.delete()
#             await state.clear()
#             return
#         text = message.text.strip()
#         # Парсим данные (разделяем по ;)
#         parts = text.split(";", 3)  # Разбиваем на 4 части максимум
#         if len(parts) != 4:
#             await message.answer("Неверный формат!")
#             return
#         tiker, quantity, price, conclusion = parts
#         d_basic = pydantic_models.Lightning(tiker=tiker, action="покупка", quantity=quantity, price=price, conclusion=conclusion)
#         now = datetime.now()
#         # Форматированная дата "д.м.г"
#         date_str = now.strftime("%Y-%m-%d")
#         # if d_light.action == "покупка":
#         stop_market_basic = round(d_basic.price * 0.994, 2)
#         stop_market_0_basic = round(d_basic.price * 1.001, 2)
#         take_profit_basic = round(d_basic.price * 1.03, 2)
#         vivod_itog="zzz"
#         # сопутствующие товары определять из словаря ичитать из гугл таблиц
#         tiker_to_dict=d_basic.tiker.upper()
#         if tiker_to_dict in dict_ticker_number:
#             i = dict_ticker_number[tiker_to_dict]
#             related_products = Read(Nazvanie_operazii="", range=f"analystrade!AI{i}")[0]
#             level_price = Read(Nazvanie_operazii="", range=f"analystrade!AI{i}")[0]
#         else:
#             related_products = "нет такого тикера!"
#             level_price = "нет данных по уровням"
#         # сделать корректно и исправить, проверить
#         plan_deistvi_basic = [[d_basic.tiker,"основной",d_basic.action,date_str,d_basic.quantity,d_basic.price,d_basic.conclusion,vivod_itog,related_products,]]
#         Dobavlenie(Nazvanie_operazii="",diapozon_dannich="основной!A5",znachenie=plan_deistvi_basic,)
#         await message.answer(f"🛑 Стоп маркет - {stop_market_basic}")
#         await message.answer(f"↔️ Безубыточность - {stop_market_0_basic}")
#         await message.answer(f"✅ Тейк-профит - {take_profit_basic}")
#         await message.answer(f"напоминаю :{level_price}")
#         await message.answer("Данные сохранены в 💹основной💹")
#         await state.clear()  # Выходим из состояния
#     except Exception as e:
#         logi.err.info(f"handle_table2_data_basic() в папке handlers/handler_message.py , Exception as e : {e}")
#   ----------------КОНЕЦ СОСТОЯНИЯ ОСНОВНОЙ---------------------


#   ----------------НАЧАЛО СОСТОЯНИЯ СОСТАВ ПОРТФЕЛЯ--------------------
# Команда /c — переключаемся в состояние для таблицы 4
# входим в состояние
@handler_message_router.message(F.text == "/c")
async def cmd_c(message: Message, state: FSMContext):
    """СОСТОЯНИЕ /c ВНОСИМ ДАННЫЕ В 💼состав💼/c"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer("работа с таблицей 💼состав💼")
        await state.set_state(UserData.TABLE_4)  # Запоминаем контекст
        await message.answer("✏️ Введите данные для 💼состав💼: строка ; действие", parse_mode="HTML")
    except Exception as e:
        logi.err.info(f"cmd_o() в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(UserData.TABLE_4)
async def handle_table4_data_basic(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return
        text = message.text.strip()
        # Парсим данные (разделяем по ;)
        parts = text.split(";", 1)  # Разбиваем на 2 части максимум
        if len(parts) != 2:
            await message.answer("Неверный формат!")
            return
        line, action = parts
        compound_pydent = pydantic_models.Сompound(line=line, action=action)
        compound_pydent_str = [[compound_pydent.action]]
        Izmenenie(
            Nazvanie_operazii="",
            diapozon_dannich=f"analystrade!AA{compound_pydent.line}",
            znachenie=compound_pydent_str,
        )
        await message.answer("Данные сохранены в 💼состав💼 в действие")
        await state.clear()  # Выходим из состояния
    except Exception as e:
        logi.err.info(f"handle_table4_data_basic() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ СОСТОЯНИЯ СОСТАВ ПОРТФЕЛЯ---------------------


#   ----------------НАЧАЛО СОСТОЯНИЯ ДДС-------------------------
@handler_message_router.message(F.text == "ДДС")
async def dds_btn(message: types.Message):
    """ДДС вся логика и ответ на вопросы"""
    if not is_admin(message.from_user.id):
        await message.delete()
        return
    await message.answer("ДДС читается...⏳")
    # Определяем текущий месяц и букву столбца
    month = datetime.now().month
    column = MONTH_TO_COLUMN.get(month)
    if not column:
        await message.answer("Ошибка: неизвестный месяц (должно быть 1-12)")
        logi.err.info("dds_btn() неизвестный месяц handlers/handler_message.py ")
        return
    # Читаем данные из таблицы
    try:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}3")[0]
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}18")[0]
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}50")[0]
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}49")[0]
        # расходы
        monthly_expenses = average_monthly(type_activity=18)
        # доходы
        monthly_income = average_monthly(type_activity=3)
    except Exception as e:
        logi.err.info(f"dds_btn() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}")
        return
    # Формируем ответ
    months_cov = round(int(dds_ostatok) / monthly_expenses, 1)
    months_covered = months_cov if months_cov > 0 else "⛔⛔⛔ Денег вообще нет. 0"
    await message.answer(
        "📊 ФИНАНСОВЫЙ ОТЧЁТ ПО ДДС\n\n"
        f"🔜Входящий поток: {format_money(dds_vchod)} ₽\n"
        f"🔙Исходящий поток: {format_money(dds_izchod)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"💵Остаток на руках: {format_money(dds_ostatok)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"🌗Хватит на: {months_covered} мес.\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"Кассовый разрыв: {format_money(dds_kassa)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"💰Средний доход в мес: {format_money(monthly_income)} ₽\n"
        f"📈Средние затраты в мес: {format_money(monthly_expenses)} ₽\n"
    )

    # Анализ кассового разрыва

    if int(dds_kassa) < 5000:
        cushion_needed = abs(int(dds_kassa)) * 3
        await message.answer(
            "🔴🔴🔴 КРИТИЧЕСКИЙ КАССОВЫЙ РАЗРЫВ!\n"
            "❗❗❗Срочные меры:\n"
            "1️⃣Ошибки в бюджете — пересмотреть приоритеты\n"
            f"2️⃣Нужна фин подушка: {format_money(cushion_needed)} ₽\n"
            "3️⃣Где можно сэкономить?\n"
            "4️⃣Где уменьшился доход и почему?\n"
            "5️⃣От каких трат можно отказаться?\n"
            "☠️ ЭТО ПРЕДЕЛ!",
            reply_markup=inlinebtn.dds_btn_detail(),
        )
    elif int(dds_kassa) < 0:
        cushion_needed = abs(int(dds_kassa)) * 3
        await message.answer(
            "🟡 КАССОВЫЙ РАЗРЫВ!\n"
            "1️⃣Баланс расходов/доходов нарушен.\n"
            "2️⃣Срочно принимайте меры!\n"
            f"3️Нужна фин подушка:{format_money(cushion_needed)} ₽\n"
            "4️⃣Где уменьшился доход и почему?\n"
            "5️⃣От каких трат можно отказаться?\n",
            reply_markup=inlinebtn.dds_btn_detail(),
        )
    else:
        await message.answer(
            "🟢 КАССОВЫЙ РАЗРЫВ ОТСУТСТВУЕТ!\nВсе платежи покрыты.\n👍", reply_markup=inlinebtn.dds_btn_detail()
        )


#   ----------------КОНЕЦ СОСТОЯНИЯ ДДС-------------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ PNL-------------------------
@handler_message_router.message(F.text == "PNL")
async def pnl_btn(message: types.Message):
    """PNL вся логика и ответ на вопросы"""
    if not is_admin(message.from_user.id):
        await message.delete()
        return
    await message.answer("PNL читается...⏳")
    # Определяем текущий месяц и букву столбца
    month = datetime.now().month
    column = MONTH_TO_COLUMN.get(month)
    if not column:
        await message.answer("Ошибка: неизвестный месяц (должно быть 1-12)")
        logi.err.info("pnl_btn() неизвестный месяц handlers/handler_message.py ")
        return
    # Читаем данные из таблицы
    try:
        pnl_income = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}52")[0]
        pnl_consumption = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}62")[0]
        pnl_ebitda = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}87")[0]
        pnl_net_profit = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}96")[0]
        pnl_net_profit_cumulative = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}97")[0]
        pnl_profitability = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}98")[0]
        pnl_gross_profit = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}106")[0]
    except Exception as e:
        logi.err.info(f"pnl_btn() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}")
        return
    # Формируем ответ
    # months_cov = round(int(dds_ostatok) / monthly_expenses, 1)
    # months_covered = months_cov if months_cov > 0 else str("⛔⛔⛔ Денег вообще нет. 0")
    await message.answer(
        "📊 ФИНАНСОВЫЙ ОТЧЁТ ПО PNL\n\n"
        f"Доход: {format_money(pnl_income)} ₽\n"
        f"Расход: {format_money(pnl_consumption)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"EBITDA: {format_money(pnl_ebitda)} ₽\n"
        f"Чистая прибыль: {format_money(pnl_net_profit)} ₽\n"
        f"Чистая прибыль с нарастающим итогом : {format_money(pnl_net_profit_cumulative)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"Рентабельность: {pnl_profitability}\n"
        f"Валовая прибыль: {pnl_gross_profit} ₽\n"
    )

    # Анализ кассового разрыва

    if int(pnl_net_profit) < 5000:
        await message.answer(
            "🔴🔴🔴 Чистая прибыль отрицательная!\n"
            "❗❗❗Срочные меры:\n"
            "1️⃣Проблемы с выручкой\n"
            "2️⃣Высокая себестоимость\n"
            "3️⃣Операционные расходы (OPEX) «съедают» маржу\n"
            "4️⃣ Финансовые и разовые факторы\n"
            "5️⃣Посчитайте точку безубыточности\n"
            "☠️ НУЖНО ДЕЙСТВОВАТЬ!!!",
            reply_markup=inlinebtn.pnl_btn_detail(),
        )
    elif int(pnl_net_profit) < 0:
        await message.answer(
            "⚠️⚠️⚠️Чистая прибыль отрицательная!\n"
            "Скоро начнутся проблемы\n"
            "1️⃣Проблемы с выручкой\n"
            "2️⃣Высокая себестоимость\n"
            "3️⃣Операционные расходы (OPEX) «съедают» маржу\n"
            "4️⃣ Финансовые и разовые факторы\n"
            "5️⃣Посчитайте точку безубыточности\n",
            reply_markup=inlinebtn.pnl_btn_detail(),
        )
    else:
        await message.answer("✅✅✅ Чистая прибыль больше 0!\n👍", reply_markup=inlinebtn.pnl_btn_detail())


#   ----------------КОНЕЦ СОСТОЯНИЯ PNL-------------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ БАЛАНС-------------------------
@handler_message_router.message(F.text == "БАЛАНС")
async def balans_btn(message: types.Message):
    """БАЛАНС вся логика и ответ на вопросы"""
    if not is_admin(message.from_user.id):
        await message.delete()
        return
    await message.answer("БАЛАНС читается...⏳")
    # Определяем текущий месяц и букву столбца
    month = datetime.now().month
    column = MONTH_TO_COLUMN.get(month)
    if not column:
        await message.answer("Ошибка: неизвестный месяц (должно быть 1-12)")
        logi.err.info("balans_btn() неизвестный месяц handlers/handler_message.py ")
        return
    # Читаем данные из таблицы
    try:
        balance_activi = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}122")[0]
        balance_passivi = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}150")[0]
        balance_sobstvennii_capital = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}151")[0]
        balance_roe = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}158")[0]
        balance_uvelichelsa_sobstvennii_capital = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}163")[0]
    except Exception as e:
        logi.err.info(f"balans_btn() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}")
        return
    # Формируем ответ
    await message.answer(
        "📊 ФИНАНСОВЫЙ ОТЧЁТ ПО БАЛАНС\n\n"
        f"АКТИВЫ: {format_money(balance_activi)} ₽\n"
        f"ПАССИВЫ: {format_money(balance_passivi)} ₽\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"ROE: {balance_roe} \n"
        f"Собственный капитал: {format_money(balance_sobstvennii_capital)} ₽\n"
        f"Увеличился собственный капитал: {format_money(balance_uvelichelsa_sobstvennii_capital)} ₽\n"
    )
    # Анализ, баланса
    if int(balance_uvelichelsa_sobstvennii_capital) < 0:
        await message.answer(
            "🔴🔴🔴 С балансом все плохо!\n"
            "❗❗❗Срочные меры:\n"
            "1️⃣ Убытки от деятельности\n"
            "2️⃣НУЖНО ПОДУМАТЬ И ВНЕСТИ ПРИЧИНЫ❗❗❗\n"
            "☠️ НУЖНО ДЕЙСТВОВАТЬ!!!",
            reply_markup=inlinebtn.balance_btn_detail(),
        )
    else:
        await message.answer(
            "✅✅✅ Увеличился собственный капитал больше 0!\nНУЖНО РАЗОБРАТСЯ В ВЫВОДАХ\n👍",
            reply_markup=inlinebtn.balance_btn_detail(),
        )


#   ----------------КОНЕЦ СОСТОЯНИЯ БАЛАНС-------------------------
#   ----------------НАЧАЛО СОСТОЯНИЯ УДАЛИТЬ ДЕЛО------------------


# Команда /d — удалить дело по номеру строки
# входим в состояние
@handler_message_router.message(F.text == "/d")
async def cmd_d(message: Message, state: FSMContext):
    """СОСТОЯНИЕ /d ВНОСИМ НОМЕР СТРОКИ"""
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer("работа с таблицей ⚙️ДЕЛА⚙️/d")
        await state.set_state(UserData.TABLE_3)  # Запоминаем контекст
        await message.answer("✏️ Введите номер строки для удаления", parse_mode="HTML")
    except Exception as e:
        logi.err.info(f"cmd_d() в папке handlers/handler_message.py , Exception as e : {e}")


@handler_message_router.message(UserData.TABLE_3)
async def deleting_row_table(message: Message, state: FSMContext):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            await state.clear()
            return
        text = message.text.strip()
        if text.isdigit():
            text = int(text)
        else:
            await message.answer("Неверный формат! Введите число.")
            return
        Delete_row(sheet_name="Дела и управление", row_index=text)
        await message.answer(f"Строка №{text} - удалена полностью ✌️ ")
        await state.clear()  # Выходим из состояния
    except Exception as e:
        logi.err.info(f"deleting_row_table() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ СОСТОЯНИЯ УДАЛИТЬ ДЕЛО-------------------
#   ----------------НАЧАЛО ДЕЛА------------------------------------
@handler_message_router.message(F.text == "⚙️ДЕЛА⚙️/d")
async def do_list(message: types.Message):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer("Рандомно дела ...⏳")
        everything_to_do = Read(Nazvanie_operazii="", range="Дела и управление!J2")[0]
        await message.answer(f"⚙️Всего дел : {everything_to_do}\n")
        random_string = str(random.randint(1, int(everything_to_do)) + 3)
        # Читаем рандомно дела
        dead_line = Read(Nazvanie_operazii="", range=f"Дела и управление!D{random_string}")[0]
        tasks = Read(Nazvanie_operazii="", range=f"Дела и управление!E{random_string}")[0]
        artificial_intelligence = Read(Nazvanie_operazii="", range=f"Дела и управление!F{random_string}")[0]
        other_information = Read(Nazvanie_operazii="", range=f"Дела и управление!G{random_string}:I{random_string}")
        await message.answer(f"⚙️ДЕЛА РАНДОМНО⚙️\n\nСтрока {random_string}\n\n{other_information}")
        await message.answer(f"{tasks}\n")
        await message.answer(f"{artificial_intelligence}\n")
        dead_line_datetime = datetime.strptime(dead_line, "%Y-%m-%d")
        now = datetime.now()
        if dead_line_datetime > now:
            await message.answer(
                f"❗Дед-лайн {dead_line_datetime.date()}❗\n"
                f"В запасе  {(dead_line_datetime - now).days} дней\n"
                f"🕰️Время есть еще...\n"
            )
        else:
            await message.answer(
                f"❗Дед-лайн {dead_line_datetime.date()}❗\n"
                f"🩸🩸🩸ПРОСРОЧЕНО на {(dead_line_datetime - now).days} дней\n"
                f"🩸Быстрее нужно делать\n"
            )
    except Exception as e:
        logi.err.info(f"do_list() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ ДЕЛА------------------------
#   ----------------НАЧАЛО ЗАПИСЬ ДЕЛА-----------------
@handler_message_router.message()
async def management(message: types.Message):
    try:
        if not is_admin(message.from_user.id):
            await message.delete()
            return
        await message.answer("работа с таблицей 💸Дела и управление💸")
        # Форматированная дата "д.м.г"
        date_str = datetime.now().strftime("%Y-%m-%d")
        text = pydantic_models.StartIndication(text=message.text.strip())
        intellig = intelligence_def(text=text.text, client=client)
        intelligence = pydantic_models.StartIndication(text=intellig)
        await message.answer(intelligence.text)
        action_plan = [
            [
                "zzz",
                date_str,
                "zzz",
                "zzz",
                text.text,
                intelligence.text,
                "zzz",
                "С+А",
                "zzz",
                "zzz",
            ]
        ]
        Dobavlenie_vstavka_strok(
            Nazvanie_operazii="",
            diapozon_dannich="Дела и управление!A5",
            znachenie=action_plan,
        )
        await message.answer("👍")
        await message.answer("ОТЛИЧНАЯ ИДЕЯ!Спасибо ХОЗЯИН", reply_markup=inlinebtn.management_btn())
    except Exception as e:
        logi.err.info(f"management() в папке handlers/handler_message.py , Exception as e : {e}")


#   ----------------КОНЕЦ ЗАПИСЬ ДЕЛА--------------------------
