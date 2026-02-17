# wallett/states.py

from aiogram.fsm.state import State, StatesGroup


class UserData(StatesGroup):
    TABLE_1 = State()  # После /com1 — ждём данные для таблицы молния
    TABLE_2 = State()  # После /com2 — ждём данные для таблицы 2


# # Можно добавить другие группы состояний:
# class AdminPanel(StatesGroup):
#     BAN_USER = State()
#     SEND_MESSAGE = State()
