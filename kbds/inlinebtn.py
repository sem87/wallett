from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def terminator_variety():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="торг день", callback_data="result_day_terminator")
    keyboard_builder.button(text="месяц", callback_data="result_month_terminator")
    keyboard_builder.button(text="что в портфеле", callback_data="briefcase")
    keyboard_builder.button(text="win_rate_terminator", callback_data="win_rate_terminator")
    keyboard_builder.button(text="резерв", callback_data="rez_terminator")
    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()


def lightning():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="итого день", callback_data="result_day")
    keyboard_builder.button(text="итого месяц", callback_data="result_month")
    keyboard_builder.button(text="win_rate", callback_data="win_rate")
    keyboard_builder.button(text="резерв1", callback_data="rez1")
    keyboard_builder.button(text="резерв2", callback_data="rez2")
    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()


def management_btn():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="рандом", callback_data="random")
    keyboard_builder.button(text="резерв1", callback_data="rez1")
    keyboard_builder.button(text="резерв2", callback_data="rez2")
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()
