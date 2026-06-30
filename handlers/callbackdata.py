# handlers/callbackdata.py

from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery

from databazesql import databaze_sql_term
from googleteable import DATA_TO_MONTH, MONTH_TO_COLUMN, Izmenenie, Read
from logi import logi
from aiogram.fsm.context import FSMContext
from handlers.handler_message import process_m_trend_days, process_m_trend_hour, process_m_trend_5min, process_m_volume, \
    process_m_btn_buy_sell
# from wallett.kbds.inlinebtn import terminator_variety, lightning  # явный импорт нужных функций
from utils import is_admin

callback_router = Router()


# ---------------------НАЧАЛО КНОПОК ДЛЯ молнии-----------------
@callback_router.callback_query(F.data == "result_month")
async def process_result_month(callback: CallbackQuery):
    """РЕЗУЛЬТАТЫ ЗА МЕСЯЦ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю данные за месяц...", show_alert=False)
        # Отправка сообщения через callback.bot
        # Определяем текущий месяц и букву столбца
        month = datetime.now().month
        column = MONTH_TO_COLUMN.get(month)
        if not column:
            logi.err.info("process_result_month() неизвестный месяц handlers/callbackdata ")
            return
        # Читаем данные из таблицы
        try:
            result_month = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}12")[0]
        except Exception as e:
            logi.err.info(f"process_result_month() ошибка ДДС,PNL handlers/callbackdata , Exception as e : {e}")
            return
        if int(result_month) > 0:
            await callback.message.answer("🏋️нужно побороть инфляцию")
            await callback.message.answer(f"молния за месяц : {result_month}")
        else:
            await callback.message.answer("🩸🩸🩸ОЧЕНЬ ПЛОХАЯ ТОРГОВЛЯ🩸🩸🩸")
            await callback.message.answer(f"молния за месяц : {result_month}")
    except Exception as e:
        logi.err.info(f"process_result_month() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "win_rate")
async def process_result_win_rate(callback: CallbackQuery):
    """win_rate"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю win_rate...", show_alert=False)
        # Отправка сообщения через callback.bot
        win_rate_sum = Read(Nazvanie_operazii="", range="молния!Q2")[0]
        calculated_risk = Read(Nazvanie_operazii="", range="молния!P2")[0]
        await callback.message.answer(f"win_rate за все время : {win_rate_sum}")
        await callback.message.answer(f"расчетный риск : {calculated_risk}")
    except Exception as e:
        logi.err.info(f"process_result_win_rate() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "rez2")
async def process_result_rez2(callback: CallbackQuery):
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


# ---------------------КОНЕЦ КНОПОК ДЛЯ молнии---------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ основной------------
@callback_router.callback_query(F.data == "result_month_basic")
async def process_result_month_basic(callback: CallbackQuery):
    """РЕЗУЛЬТАТЫ ЗА МЕСЯЦ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю данные за месяц...", show_alert=False)
        # Отправка сообщения через callback.bot
        # Определяем текущий месяц и букву столбца
        month = datetime.now().month
        column = MONTH_TO_COLUMN.get(month)
        if not column:
            logi.err.info("process_result_month_basic() неизвестный месяц handlers/callbackdata ")
            return
        # Читаем данные из таблицы
        try:
            result_month = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}13")[0]
        except Exception as e:
            logi.err.info(f"process_result_month_basic() ошибка ДДС,PNL handlers/callbackdata , Exception as e : {e}")
            return
        if int(result_month) > 0:
            await callback.message.answer("🏋️нужно побороть инфляцию")
            await callback.message.answer(f"основной за месяц : {result_month}")
        else:
            await callback.message.answer("🩸🩸🩸ОЧЕНЬ ПЛОХАЯ ТОРГОВЛЯ🩸🩸🩸")
            await callback.message.answer(f"основной за месяц : {result_month}")
    except Exception as e:
        logi.err.info(f"process_result_month_basic() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "win_rate_basic")
async def process_result_win_rate_basic(callback: CallbackQuery):
    """win_rate"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю win_rate...", show_alert=False)
        # Отправка сообщения через callback.bot
        win_rate_sum = Read(Nazvanie_operazii="", range="основной!Q2")[0]
        calculated_risk = Read(Nazvanie_operazii="", range="основной!P2")[0]
        await callback.message.answer(f"win_rate за все время : {win_rate_sum}")
        await callback.message.answer(f"расчетный риск : {calculated_risk}")
    except Exception as e:
        logi.err.info(f"process_result_win_rate_basic() в папке handlers/callbackdata , Exception as e : {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ основной-------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ terminator----------
@callback_router.callback_query(F.data == "result_day_terminator")
async def result_day_terminator_def(callback: CallbackQuery):
    """РЕЗУЛЬТАТЫ ЗА ДЕНЬ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("terminator за день...", show_alert=False)
        # Отправка сообщения через callback.bot
        await callback.message.answer("РЕЗУЛЬТАТЫ ЗА ДЕНЬ")

        rows_day = databaze_sql_term.total_trade_by_day()
        for row_day in rows_day:
            await callback.message.answer(
                f"🖊️Дата - {row_day['sale_date']}\n"
                f"Итого : {round(row_day['total_net'], 1)} р\n"
                f"📊Процент : {row_day['total_percent']}%\n"
            )

    except Exception as e:
        logi.err.info(f"result_day_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "result_month_terminator")
async def result_month_terminator_def(callback: CallbackQuery):
    """РЕЗУЛЬТАТЫ ЗА МЕСЯЦ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("terminator за месяц...", show_alert=False)
        # Отправка сообщения через callback.bot
        await callback.message.answer("РЕЗУЛЬТАТЫ ЗА МЕСЯЦ")
        rows_month = databaze_sql_term.total_trade_by_moth()
        for row_month in rows_month:
            await callback.message.answer(
                f"🖊️Дата - {row_month['sale_month']}\n"
                f"Итого : {round(row_month['total_net'], 1)} р\n"
                f"🤝Количество сделок : {row_month['deals_count']}шт\n"
            )
            strok = DATA_TO_MONTH[row_month["sale_month"]]
            Izmenenie(
                Nazvanie_operazii="",
                diapozon_dannich=f"terminator!A{strok}:C{strok}",
                znachenie=[[row_month["sale_month"], round(row_month["total_net"], 1), row_month["deals_count"]]],
            )
    except Exception as e:
        logi.err.info(f"result_month_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "win_rate_terminator")
async def win_rate_terminator_def(callback: CallbackQuery):
    """win_rate"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю win_rate...", show_alert=False)
        # Отправка сообщения через callback.bot
        await callback.message.answer("win_rate")
        await callback.message.answer("🔵🔵🔵")
    except Exception as e:
        logi.err.info(f"win_rate_terminator_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "briefcase")
async def briefcase_def(callback: CallbackQuery):
    """ЧТО В ПОРТФЕЛЕ"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # Правильное подтверждение нажатия кнопки
        await callback.answer("ЧТО В ПОРТФЕЛЕ...", show_alert=False)
        # Отправка сообщения через callback.bot
        await callback.message.answer("ЧТО В ПОРТФЕЛЕ")
        rows_briefcase = databaze_sql_term.what_in_briefcase()
        for row_briefcase in rows_briefcase:
            await callback.message.answer(
                f"📝Тикер - {row_briefcase['tiker']}\n"
                f"Кол-во : {row_briefcase['quantity_buy']} шт\n"
                f"Цена покупки : {row_briefcase['buy_price']}р\n"
            )
    except Exception as e:
        logi.err.info(f"briefcase_def() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "rez_terminator")
async def process_result_rez_terminator(callback: CallbackQuery):
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
async def process_management(callback: CallbackQuery):
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
# ---------------------НАЧАЛО КНОПОК ДЛЯ ДДС-----------------
@callback_router.callback_query(F.data == "incoming_flow_details")
async def dds_btn_incoming_flow_details(callback: CallbackQuery):
    """Входящий поток подробно"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю входящий поток подробно...", show_alert=False)
        await callback.message.answer("🔜Входящий поток подробно : ")
        # Определяем текущий месяц и букву столбца
        month = datetime.now().month
        column = MONTH_TO_COLUMN.get(month)
        if not column:
            logi.err.info("dds_btn_incoming_flow_details() неизвестный месяц handlers/callbackdata ")
            return
        # Читаем данные из таблицы
        try:
            dds_zarplata = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}5")[0]
            dds_prochee = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}6")[0]
            dds_terminator = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}11")[0]
            dds_molnia = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}12")[0]
            dds_osnovnoi = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}13")[0]
        except Exception as e:
            logi.err.info(f"pnl_btn() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}")
            return
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer(
            f"Зарплата : {dds_zarplata}\n"
            f"Прочее : {dds_prochee}\n"
            f"➖➖➖➖➖➖➖➖➖➖➖\n"
            f"terminator : {dds_terminator}\n"
            f"молния : {dds_molnia}\n"
            f"основной : {dds_osnovnoi}\n"
        )
    except Exception as e:
        logi.err.info(f"dds_btn_incoming_flow_details() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "outgoing_flow_details")
async def dds_btn_outgoing_flow_details(callback: CallbackQuery):
    """Исходящий поток подробно"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю исходящий поток подробно...", show_alert=False)
        await callback.message.answer("🔙Исходящий поток подробно : ")
        # Определяем текущий месяц и букву столбца
        month = datetime.now().month
        column = MONTH_TO_COLUMN.get(month)
        if not column:
            logi.err.info("dds_btn_outgoing_flow_details() неизвестный месяц handlers/callbackdata ")
            return
        # Читаем данные из таблицы
        try:
            dds_avtomobil_zapchasti = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}20")[0]
            dds_azs = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}21")[0]
            dds_apteka = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}22")[0]
            dds_zkh = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}23")[0]
            dds_ippoteka = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}24")[0]
            dds_manikur_strizka = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}25")[0]
            dds_marketplase = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}26")[0]
            dds_obrazovanie_schkola = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}27")[0]
            dds_produkti_rinok = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}28")[0]
            dds_prochee_rashod = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}29")[0]
            dds_rezerv_biznes = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}30")[0]
            dds_supermarket = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}31")[0]
            dds_trenirovka = Read(Nazvanie_operazii="", range=f"ДДС,PNL!{column}32")[0]

        except Exception as e:
            logi.err.info(
                f"dds_btn_outgoing_flow_details() ошибка чтения таблицы ДДС,PNL handlers/handler_message.py , Exception as e : {e}"
            )
            return
        # ✅ Отправка сообщения через callback.bot
        await callback.message.answer(
            f"автомобиль запчасти : {dds_avtomobil_zapchasti}\n"
            f"азс : {dds_azs}\n"
            f"аптека : {dds_apteka}\n"
            f"жкх : {dds_zkh}\n"
            f"ипотека : {dds_ippoteka}\n"
            f"маникюр стрижки : {dds_manikur_strizka}\n"
            f"маркетплейсы : {dds_marketplase}\n"
            f"образование школа : {dds_obrazovanie_schkola}\n"
            f"продукты рынок : {dds_produkti_rinok}\n"
            f"прочее : {dds_prochee_rashod}\n"
            f"резерв бизнес : {dds_rezerv_biznes}\n"
            f"супермаркет : {dds_supermarket}\n"
            f"тренировка : {dds_trenirovka}\n"
        )
    except Exception as e:
        logi.err.info(f"dds_btn_outgoing_flow_details() в папке handlers/callbackdata , Exception as e : {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ ДДС-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ PNL-----------------
@callback_router.callback_query(F.data == "income_details")
async def pnl_btn_income_details(callback: CallbackQuery):
    """Доходы подробно"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю доходы подробно...", show_alert=False)
        await callback.message.answer("Доходы подробно : ")
        await callback.message.answer("ПОЯВИТСЯ БИЗНЕС ИЛИ ПЕРЕМЕННЫЕ РАСХОДЫ ДОБАВИЩЬ ЛОГИКУ")
    except Exception as e:
        logi.err.info(f"pnl_btn_income_details() в папке handlers/callbackdata , Exception as e : {e}")


@callback_router.callback_query(F.data == "expenses_detail")
async def pnl_btn_expenses_detail(callback: CallbackQuery):
    """Расходы подробно"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Загружаю расходы подробно...", show_alert=False)
        await callback.message.answer("Расходы подробно : ")
        await callback.message.answer("ПОЯВИТСЯ БИЗНЕС ИЛИ ПЕРЕМЕННЫЕ РАСХОДЫ ДОБАВИЩЬ ЛОГИКУ")
    except Exception as e:
        logi.err.info(f"pnl_btn_expenses_detail() в папке handlers/callbackdata , Exception as e : {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ PNL-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ ОТМЕНА----------------
@callback_router.callback_query(F.data == "cancel_fsm")
async def cancel_fsm_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки отмены для FSM"""
    try:
        if not is_admin(callback.from_user.id):
            await callback.message.delete()
            return
        # ✅ Правильное подтверждение нажатия кнопки
        await callback.answer("Операция отменена", show_alert=False)
        # Очищаем состояние FSM
        await state.clear()
        # Редактируем сообщение, чтобы убрать кнопку
        try:
            await callback.message.edit_text("❌ Операция отменена.Вы вышли из режима заполнения.")
        except Exception as e:
            logi.err.info(f"cancel_fsm_handler() в handlers/callbackdata в убрать кнопку, Exception as e: {e}")
            await callback.message.answer("❌ Операция отменена.")
    except Exception as e:
        logi.err.info(f"cancel_fsm_handler() в папке handlers/callbackdata, Exception as e: {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ ОТМЕНА-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ вверх/вниз ДЕНЬ----------------
@callback_router.callback_query(F.data == "up_days")
async def direction_up_handler_days(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вверх'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вверх 📈", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_day="вверх")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_days(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_up_handler_days() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "down_days")
async def direction_down_handler_days(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вниз'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вниз 📉", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_day="вниз")
        # Может делать комент а кнопку уничтожать ??????????????
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_days(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_down_handler_days() в папке handlers/callbackdata, Exception as e: {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ вверх/вниз ДЕНЬ-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ вверх/вниз ЧАС----------------
@callback_router.callback_query(F.data == "up_hour")
async def direction_up_handler_hour(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вверх'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вверх 📈", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_hour="вверх")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_hour(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_up_handler_hour() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "down_hour")
async def direction_down_handler_hour(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вниз'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вниз 📉", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_hour="вниз")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_hour(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_down_handler_hour() в папке handlers/callbackdata, Exception as e: {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ вверх/вниз ЧАС-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ вверх/вниз 5МИН----------------
@callback_router.callback_query(F.data == "up_5min")
async def direction_up_handler_5min(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вверх'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вверх 📈", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_5min="вверх")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_5min(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_up_handler_5min() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "down_5min")
async def direction_down_handler_5min(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки 'вниз'"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: вниз 📉", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_5min="вниз")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_5min(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_down_handler_5min() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "dno_max")
async def direction_dno_max_handler_5min(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки дно или max"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("дно/max", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(trend_5min="дно/max")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_trend_5min(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_dno_max_handler_5min() в папке handlers/callbackdata, Exception as e: {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ вверх/вниз 5МИН-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ объем----------------
@callback_router.callback_query(F.data == "volume_short")
async def direction_volume_short(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки объем низкий"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: объем низкий", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(volume="низкий")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_volume(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_volume_short() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "volume_average")
async def direction_volume_average(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки объем средний"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: объем средний", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(volume="средний")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_volume(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_volume_average() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "volume_above_average")
async def direction_volume_above_average(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки объем выше среднего"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: объем выше среднего", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(volume="выше среднего")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_volume(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_volume_above_average() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "volume_super")
async def direction_volume_super(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки объем огромный"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: объем огромный", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(volume="огромный")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_volume(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_volume_super() в папке handlers/callbackdata, Exception as e: {e}")


# ---------------------КОНЕЦ КНОПОК ДЛЯ объем-----------------
# ---------------------НАЧАЛО КНОПОК ДЛЯ покупка/продажа----------------
@callback_router.callback_query(F.data == "btn_buy")
async def direction_btn_buy(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки покупка"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: покупка", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(btn_buy_sell="покупка")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_btn_buy_sell(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_btn_buy() в папке handlers/callbackdata, Exception as e: {e}")


@callback_router.callback_query(F.data == "btn_sell")
async def direction_btn_sell(callback: CallbackQuery, state: FSMContext):
    """Обработчик кнопки продажа"""
    try:
        # ✅ Подтверждение нажатия
        await callback.answer("Выбрал: продажа", show_alert=False)
        # ✅ Сохраняем значение в FSM
        await state.update_data(btn_buy_sell="продажа")
        # ⚡ ВЫЗЫВАЕМ ФУНКЦИЮ НАПРЯМУЮ
        # Передаем callback.message, так как функция ждет объект Message
        await process_m_btn_buy_sell(callback.message, state)
    except Exception as e:
        logi.err.info(f"direction_btn_sell() в папке handlers/callbackdata, Exception as e: {e}")
# ---------------------КОНЕЦ КНОПОК ДЛЯ покупка/продажа-----------------
