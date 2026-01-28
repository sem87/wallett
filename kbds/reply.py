from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выручка ГНОМ"), KeyboardButton(text="Запас ГЕЛИЯ")],
        [
            KeyboardButton(text="ДДС"),
            KeyboardButton(text="PNL"),
        ],
        [
            KeyboardButton(text="БАЛАНС"),  # Средний чек,кол-во покупок
            KeyboardButton(text="Категории продаж"),
        ],
        [
            KeyboardButton(text="НАЛОГ"),
            KeyboardButton(text="ПОГОДА"),
        ],
        [
            KeyboardButton(text="ПОСЕЩЕНИЕ"),
            KeyboardButton(text="ДЕЛА"),
        ],
    ],
    # is_persistent=True,
    resize_keyboard=True,
    input_field_placeholder="ИДЕЯ",
)
