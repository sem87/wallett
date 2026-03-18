from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="необх финансы"), KeyboardButton(text="БАЛАНС")],
        [KeyboardButton(text="ДДС"), KeyboardButton(text="PNL")],
        [KeyboardButton(text="🦾terminator🦾"), KeyboardButton(text="⚡молния⚡/m")],
        [
            KeyboardButton(text="💹основной💹/o"),
            KeyboardButton(text="💼состав💼/c"),
        ],
        [
            KeyboardButton(text="⚙️ДЕЛА⚙️/d"),
        ],
    ],
    # is_persistent=True,
    resize_keyboard=True,
    input_field_placeholder="ИДЕЯ",
)
