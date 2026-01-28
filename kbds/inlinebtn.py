from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Выручка ГНОМ мес", callback_data="viruchka_GNOM")
    keyboard_builder.button(text="Выручка Шардом мес", callback_data="viruchka_CHARDOM")
    keyboard_builder.button(
        text="Выр МАРКЕТПЛ мес", callback_data="viruchka_MARKETPLASE"
    )
    keyboard_builder.button(
        text="ПАССИВНЫЙ ДОХОД мес", callback_data="passivnii_dochod"
    )
    keyboard_builder.button(
        text="КОРПОРАЦИЯ РОБОТОВ мес", callback_data="korporazia_robotov"
    )
    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()


def pogoda_vivod():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="ВЫВОД О ПОГОДЕ", callback_data="pogoda_vivodi")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def poseshenie():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="ПОСЕЩЕНИЕ ПОДРОБНО", callback_data="posesheni")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


# def pogoda():
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.button(text='Доход ШарДом', callback_data='vvod_dochod_CHARDOM')
#     keyboard_builder.button(text='ТРАТИМ из ЗАРПЛАТЫ', callback_data='tratim_iz_zarplati')
#     keyboard_builder.button(text='Закупка ОДЕЖДЫ', callback_data='zakupka_odezdi')
#     keyboard_builder.button(text='Закупка ИГРУШКИ', callback_data='zakupka_igrushki')
#     keyboard_builder.button(text='Закупка ШАРИКИ ГНОМ', callback_data='zakupka_shariki_GNOM')
#     keyboard_builder.button(text='Закупка ШАРИКИ ДОМ', callback_data='zakupka_shariki_DOM')
#     keyboard_builder.adjust(2, 2)
#     return keyboard_builder.as_markup()
