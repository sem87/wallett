# wallett/states.py

from aiogram.fsm.state import State, StatesGroup


class UserData(StatesGroup):
    TABLE_1 = State()  # После /m — ждём данные для таблицы молния
    # ======начало состояния для основной ======
    #TABLE_2 = State()  # После /o — ждём данные для таблицы основной
    # TABLE_2 = State()  # Старое состояние можно удалить
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
