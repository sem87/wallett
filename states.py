# wallett/states.py

from aiogram.fsm.state import State, StatesGroup


class UserData(StatesGroup):
    # ======начало состояния для молния ========
    # TABLE_1 = State()  # После /m — ждём данные для таблицы молния
    TABLE_1_TICKER = State()  # Шаг 1: Ожидание тикера
    TABLE_1_BUY_OR_SELL = State()  # Шаг 1.2: Ожидание ПОКУПКА ИЛИ ПРОДАЖА
    TABLE_1_NEWS = State()  # Шаг 2: Ожидание новости
    TABLE_1_TREND_DAYS = State()  # Шаг 3: Ожидание тренд день
    TABLE_1_TREND_HOUR = State()  # Шаг 4: Ожидание тренд час
    TABLE_1_TREND_5MIN = State()  # Шаг 5: Ожидание тренд 5мин
    TABLE_1_ATTENDANT = State()  # Шаг 6: Ожидание сопутствующие
    TABLE_1_VOLUME = State()  # Шаг 7: Ожидание объем
    TABLE_1_CUP = State()  # Шаг 8: Ожидание стакан
    #TABLE_1_PATTERN = State()  # Шаг 9: Ожидание паттерна
    TABLE_1_CONCLUSION = State()  # Шаг 10: Ожидание вывода/заключения
    TABLE_1_QUANTITY = State()    # Шаг 11: Ожидание количества
    TABLE_1_PRICE = State()       # Шаг 12: Ожидание цены
    # ======конец состояния для молния =========
    # ======начало состояния для основной ======
    TABLE_2_TICKER = State()      # Шаг 1: Ожидание тикера
    TABLE_2_QUANTITY = State()    # Шаг 2: Ожидание количества
    TABLE_2_PRICE = State()       # Шаг 3: Ожидание цены
    TABLE_2_CONCLUSION = State()  # Шаг 4: Ожидание вывода/заключения
    # ======конец состояния для основной =======
    TABLE_3 = State()  # После /d — ждём номер строки для удаления
    TABLE_4 = State()  # После /c — ждём номер строки для удаления


# # Можно добавить другие группы состояний:
# class AdminPanel(StatesGroup):
#     BAN_USER = State()
#     SEND_MESSAGE = State()
