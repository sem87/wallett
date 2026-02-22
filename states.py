# wallett/states.py

from aiogram.fsm.state import State, StatesGroup


class UserData(StatesGroup):
    TABLE_1 = State()  # После /m — ждём данные для таблицы молния
    TABLE_2 = State()  # После /o — ждём данные для таблицы основной
    TABLE_3 = State()  # После /d — ждём номер строки для удаления


# # Можно добавить другие группы состояний:
# class AdminPanel(StatesGroup):
#     BAN_USER = State()
#     SEND_MESSAGE = State()
