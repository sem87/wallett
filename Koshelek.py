from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
import asyncio
import random
from datetime import datetime, timedelta
from dotenv import find_dotenv, load_dotenv


from googleteable import *
from googleteable2table import *
from kbds import inlinebtn, reply


"""СТОРОННИЕ СЕРВИСЫ"""
"""___  ДАННЫЕ.ВХОДНЫЕ ПАРАМЕТРЫ  ___"""
load_dotenv(".env.wallet")
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()
my_admins_list = os.getenv("my_admins")
my_admins_list_2 = os.getenv("my_admins2")
month_dict = {
    1: "ЯНВАРЬ",
    2: "ФЕВРАЛЬ",
    3: "МАРТ",
    4: "АПРЕЛЬ",
    5: "МАЙ",
    6: "ИЮНЬ",
    7: "ИЮЛЬ",
    8: "АВГУСТ",
    9: "СЕНТЯБРЬ",
    10: "ОКТЯБРЬ",
    11: "НОЯБРЬ",
    12: "ДЕКАБРЬ",
}

""" ФИЛЬТРЫ МЕНЮ """


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    if (
            int(message.from_user.id) == int(my_admins_list)
            or int(message.from_user.id) == int(my_admins_list_2)
    ):
        await message.answer("ПРИВЕТ!!!Я КОШЕЛЕК", reply_markup=reply.start_kb)
    else:
        await message.delete()


# """УЧЕТКА АДМИНКИ ЗАКОНЧИЛАСЬ СТАРТ"""
#

# @dp.message(Command("menu"))
# async def start_cmd(message: types.Message):
#     await message.answer('БУДЕТ СЛЕДУЮЩЕЕ МЕНЮ : ')
#
#
# @dp.message(Command("problema"))
# async def start_cmd(message: types.Message):
#     """ЗАПИСЫВАЕТ ПРОБЛЕМУ В ПЛАН ДЕЙСТВИЙ"""
#     await message.answer('ВНЕСИТЕ СВОЮ ПРОБЛЕМУ В РАЗРАБОТКУ : ')
#
#
# @dp.message(Command("pusto"))
# async def start_cmd(message: types.Message):
#     await message.answer('МЕСТО ПУСТОЕ : ')


"""СЛУШАЕТ НАЖАТИЕ КНОПОК КЕЙБОРД"""


@dp.message(F.text == "финансы")
async def reply_btn(message: types.Message):
    itogo = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!H1")
    bn = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!J1")
    await message.answer("ВЫРУЧКА СЕГОДНЯ : " + itogo[0] + " руб")
    await message.answer("Б/Н : " + bn[0] + " руб")
    if int(itogo[0]) < 7700:
        await message.answer(
            "ПОДНАЖМИ!!!\nБОРДОВЫЙ 🆘\nДо следующего :"
            + str(7700 - int(itogo[0]))
            + " руб"
        )
    elif int(itogo[0]) < 11000:
        await message.answer(
            "НЕ ДОСТАТОЧНО!!!\nТЕМНО-КРАСНЫЙ 🆘\nДо следующего :"
            + str(11000 - int(itogo[0]))
            + " руб"
        )
    elif int(itogo[0]) < 17900:
        await message.answer(
            "КРАСНЫЙ 🟥\nДо следующего :" + str(17900 - int(itogo[0])) + " руб"
        )
        await message.answer("🦾")
    elif int(itogo[0]) < 24900:
        await message.answer(
            "ЖЕЛТЫЙ 🟨\nДо следующего :" + str(24900 - int(itogo[0])) + " руб"
        )
        await message.answer("🤟")
    elif int(itogo[0]) < 31600:
        await message.answer(
            "ЗЕЛЕНЫЙ 🟩\nДо следующего :" + str(31600 - int(itogo[0])) + " руб"
        )
        await message.answer("🏆")
    elif int(itogo[0]) < 38500:
        await message.answer(
            "🤩" + "СИНИЙ 🟦\nДо следующего :" + str(38500 - int(itogo[0])) + " руб"
        )
        await message.answer("🤩")
    else:
        await message.answer("УРОВЕНЬ БОГ" + "😇")
        await message.answer("😇")
    now = datetime.now()
    end_of_day = now.replace(hour=19, minute=0)
    await message.answer(
        "Время осталось : " + str(end_of_day - now) + "ч",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


@dp.message(F.text == "terminator")
async def reply_btn(message: types.Message):
    # gel_gnom = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!M1")
    # await message.answer("ОСТАТОК Гелия ГНОМ : " + gel_gnom[0])
    await message.answer("нужно строить логику terminator", reply_markup=inlinebtn.terminator_variety())




@dp.message(F.text == "ДДС")
async def reply_btn(message: types.Message):
    now = datetime.now().month
    if now == 1:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!B3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!B16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!B53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!B52")
    elif now == 2:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!C3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!C16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!C53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!C52")
    elif now == 3:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!D3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!D16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!D53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!D52")
    elif now == 4:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!E3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!E16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!E53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!E52")
    elif now == 5:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!F3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!F16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!F53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!F52")
    elif now == 6:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!G3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!G16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!G53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!G52")
    elif now == 7:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!H3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!H16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!H53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!H52")
    elif now == 8:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!I3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!I16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!I53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!I52")
    elif now == 9:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!J3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!J16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!J53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!J52")
    elif now == 10:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!K3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!K16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!K53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!K52")
    elif now == 11:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!L3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!L16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!L53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!L52")
    elif now == 12:
        dds_vchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!M3")
        dds_izchod = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!M16")
        dds_kassa = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!M53")
        dds_ostatok = Read(Nazvanie_operazii="ЧИТАЕМ ДДС ", range="ДДС,PNL!M52")
    else:
        await message.answer("ПИЗДЕШЬ КАКОЙ ТО ,МЕСЯЦЕВ 12 ТОЛЬКО")
    await message.answer("ВХОДЯЩИЙ ДЕНЕЖНЫЙ ПОТОК : " + dds_vchod[0])
    await message.answer("ИСХОДЯЩИЙ ДЕНЕЖНЫЙ ПОТОК : " + dds_izchod[0])
    await message.answer("ОСТАТОК ДЕНЕГ НА РУКАХ : " + dds_ostatok[0])
    await message.answer(
        "ДЕНЕГ ХВАТИТ НА : " + str(round(int(dds_ostatok[0]) / 77000, 1)) + "МЕСЯЦЕВ"
    )
    await message.answer("КАССОВЫЙ РАЗРЫВ : " + dds_kassa[0])
    if int(dds_kassa[0]) < -5000:  # почему такая цифра? исходя из
        await message.answer("НУЖНО РАЗОБРАТЬСЯ В ПРИЧИНАХ КАССОВОГО РАЗРЫВА!!!")
        await message.answer(
            "1)ТОВАР КОПИТСЯ НА СКЛАДЕ ошибки в закупках,нужно проанализировать его продажу"
        )
        await message.answer(
            "2)закупаем МНОГО СЕЗОННОГО ТОВАРА — значит, надо уменьшить объем закупки и устроить распродажу"
        )
        await message.answer("3)Ошибки при планировании бюджета,создать приоретет")
        await message.answer(
            "4)НЕОБХОДИМА ФИНАНСОВАЯ ПОДУШКА : "
            + str(int(dds_kassa[0]) * (-3))
            + " руб"
        )
        await message.answer("5) НА ЧЕМ МОЖНО СЭКОНОМИТЬ ???")
        await message.answer("6) ГДЕ ПЕРЕСТАЛИ ПЛАТИТЬ ?ПОЧЕМУ?")
        await message.answer("ЭТО ПРЕДЕЛ!!!")
        await message.answer("☠️")
    elif int(dds_kassa[0]) < 0:
        await message.answer(
            "ХОЗЯИН У НАС КАССОВЫЙ РАЗРЫВ !!!баланс расходов и доходов нарушен"
        )
        await message.answer("разберись в причинах!!!СРОЧНО ПРИНИМАЙ МЕРЫ")
        await message.answer(
            "НЕОБХОДИМА ФИНАНСОВАЯ ПОДУШКА : " + str(int(dds_kassa[0]) * (-3)) + " руб"
        )
        await message.answer("🫵")
    else:
        await message.answer("ХОЗЯИН КАССОВОГО РАЗРЫВА НЕТ !!!ВСЕ ГУД")
        await message.answer("ДЕНЕГ ХВАТАЕТ ЧТОБЫ ЗА ВСЕ РАСЧИТАТЬСЯ!!!")
        await message.answer("👍")


@dp.message(F.text == "PNL")
async def reply_btn(message: types.Message):
    now = datetime.now().month
    if now == 1:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B105"
        )
    elif now == 2:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B105"
        )
    elif now == 3:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C105"
        )
    elif now == 4:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D105"
        )
    elif now == 5:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E105"
        )
    elif now == 6:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F105"
        )
    elif now == 7:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G105"
        )
    elif now == 8:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H105"
        )
    elif now == 9:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I105"
        )
    elif now == 10:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J105"
        )
    elif now == 11:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K105"
        )
    elif now == 12:
        pnl_dochod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M55")
        pnl_raschod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M66")
        pnl_ebitda = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M94")
        pnl_chista_pribil = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M103")
        pnl_rentabilnost_now = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M105")
        pnl_rentabilnost_proschlii_mesiaz = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L105"
        )
    else:
        await message.answer("ПИЗДЕШЬ КАКОЙ ТО ,МЕСЯЦЕВ 12 ТОЛЬКО")
    await message.answer("ДОХОД : " + pnl_dochod[0])
    await message.answer("РАСХОД : " + pnl_raschod[0])
    await message.answer("EBITDA (Произв. приб. - косв. расх) : " + pnl_ebitda[0])
    await message.answer("ЧИСТАЯ ПРИБЫЛЬ : " + pnl_chista_pribil[0])
    if int(pnl_chista_pribil[0]) < -10000:  # почему такая цифра? исходя из чего
        await message.answer("ШЕВЕЛИ ЖОПОЙ И МОЗГАМИ ОДНОВРЕМЕННО!!!")
        await message.answer("ЭТО ПРЕДЕЛ!!!")
        await message.answer("🤬")
    elif int(pnl_chista_pribil[0]) < 0:
        await message.answer("ХОЗЯИН МЫ НЕ ЗАРАБАТЫВАЕМ СОВСЕМ!!!")
        await message.answer("ПРОВЕДИ ДЕТАЛЬНЫЙ АНАЛИЗ ДОХОДОВ И РАСХОДОВ")
        await message.answer("КАКИЕ ПРИЧИНЫ У ЭТОГО :")
        await message.answer("1)Устраивать акции")
        await message.answer("2)Переключаться на другие товары и услуги")
        await message.answer("3)Продавайте с минимальной наценкой")
        await message.answer("😬")
    elif int(pnl_chista_pribil[0]) < 27000:  # почему такая цифра? исходя из чего
        await message.answer("🫵")
        await message.answer("ЧИСТАЯ ПРИБЫЛЬ НЕ ДОТЯГИВАЕТ ДО ПЛАНА!!!")
        await message.answer(
            "ОСТАЛОСЬ : " + str(27000 - int(pnl_chista_pribil[0])) + "руб"
        )
    else:
        await message.answer("ЧИСТАЯ ПРИБЫЛЬ В НОРМЕ!!!")
        await message.answer("👏")
    await message.answer(
        "РЕНТАБИЛЬНОСТЬ (сколько денег с каждого вложенного руб) : "
        + pnl_rentabilnost_now[0]
    )
    await message.answer(
        "РЕНТАБИЛЬНОСТЬ за прошлый месяц : " + pnl_rentabilnost_proschlii_mesiaz[0]
    )
    if float(pnl_rentabilnost_now[0]) > float(pnl_rentabilnost_proschlii_mesiaz[0]):
        await message.answer("КОМПАНИЯ РАЗВИВАЕТСЯ.ДЕЛА ИДУТ В ГОРУ")
    else:
        await message.answer("КОМПАНИЯ ДЕГРОДИРУЕТ")


@dp.message(F.text == "БАЛАНС")
async def reply_btn(message: types.Message):
    now = datetime.now().month
    if now == 1:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!B174"
        )
    elif now == 2:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!C174"
        )
    elif now == 3:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!D174"
        )
    elif now == 4:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!E174"
        )
    elif now == 5:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!F174"
        )
    elif now == 6:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!G174"
        )
    elif now == 7:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!H174"
        )
    elif now == 8:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!I174"
        )
    elif now == 9:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!J174"
        )
    elif now == 10:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!K174"
        )
    elif now == 11:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!L174"
        )
    elif now == 12:
        balance_active = Read(Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M129")
        balance_active_oborotnii = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M130"
        )
        balance_sobstvennii_kapital = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="ДДС,PNL!M174"
        )
    else:
        await message.answer("ПИЗДЕШЬ КАКОЙ ТО ,МЕСЯЦЕВ 12 ТОЛЬКО")
    await message.answer("АКТИВ : " + balance_active[0])
    await message.answer(
        "Оборотные активы (сколько денег уже участвует) : "
        + balance_active_oborotnii[0]
    )
    await message.answer("СОБСТВЕННЫЙ  капитал : " + balance_sobstvennii_kapital[0])


@dp.message(F.text == "Категории продаж")
async def reply_btn(message: types.Message):
    now = datetime.now().month
    if now == 1:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q18")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R18")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S18")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W18"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X18")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y18"
        )
    elif now == 2:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q19")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R19")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S19")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W19"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X19")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y19"
        )
    elif now == 3:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q20")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R20")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S20")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W20"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X20")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y20"
        )
    elif now == 4:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q21")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R21")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S21")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W21"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X21")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y21"
        )
    elif now == 5:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q22")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R22")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S22")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W22"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X22")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y22"
        )
    elif now == 6:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q23")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R23")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S23")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W23"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X23")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y23"
        )
    elif now == 7:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q24")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R24")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S24")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W24"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X24")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y24"
        )
    elif now == 8:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q25")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R25")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S25")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W25"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X25")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y25"
        )
    elif now == 9:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q26")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R26")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S26")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W26"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X26")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y26"
        )
    elif now == 10:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q27")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R27")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S27")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W27"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X27")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y27"
        )
    elif now == 11:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q28")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R28")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S28")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W28"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X28")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y28"
        )
    elif now == 12:
        kategorii_igrushkiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q29")
        kategorii_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R29")
        kategorii_sharikiGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S29")
        kategorii_roe_igrushkiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!W29"
        )
        kategorii_roe_odezdaGNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!X29")
        kategorii_roe_sharikiGNOM = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Y29"
        )
    else:
        await message.answer("ПИЗДЕШЬ КАКОЙ ТО ,МЕСЯЦЕВ 12 ТОЛЬКО")
    itogo = (
            float(kategorii_igrushkiGNOM[0])
            + float(kategorii_odezdaGNOM[0])
            + float(kategorii_sharikiGNOM[0])
    )
    await message.answer("ПРОДАЛИ Игрушки ГНОМ : " + kategorii_igrushkiGNOM[0] + " руб")
    await message.answer("ПРОДАЛИ Одежда ГНОМ : " + kategorii_odezdaGNOM[0] + " руб")
    await message.answer("ПРОДАЛИ Шарики ГНОМ : " + kategorii_sharikiGNOM[0] + " руб")
    await message.answer(
        "Игрушк ГНОМ : "
        + str(round(float(kategorii_igrushkiGNOM[0]) * 100 / itogo, 2))
        + " %"
        + " ; ROE = "
        + kategorii_roe_igrushkiGNOM[0]
    )
    await message.answer(
        "Одежда ГНОМ : "
        + str(round(float(kategorii_odezdaGNOM[0]) * 100 / itogo, 2))
        + " %"
        + " ; ROE = "
        + kategorii_roe_odezdaGNOM[0]
    )
    await message.answer(
        "Шарики ГНОМ : "
        + str(round(float(kategorii_sharikiGNOM[0]) * 100 / itogo, 2))
        + " %"
        + " ; ROE = "
        + kategorii_roe_sharikiGNOM[0]
    )


@dp.message(F.text == "НАЛОГ")
async def reply_btn(message: types.Message):
    nalog = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!I5")
    await message.answer("НАЛОГ ДОЛГ : " + nalog[0] + " руб")
    if int(nalog[0]) > 30000:
        await message.answer("ХЮСТОН, У НАС ПРОБЛЕМЫ !ПЛАТИ НАЛОГ")
        await message.answer("🤯")
    else:
        await message.answer("С НАЛОГОМ ВСЕ ПОД КОНТРОЛЕМ!")


@dp.message(F.text == "ПОСЕЩЕНИЕ")
async def reply_btn(message: types.Message):
    await message.answer("РЕКОРД ЗА ГОД ПО СУММ ЧЕЛ")
    """НАХОДИМ РЕКОРД ПОКАЗАТЕЛЕЙ ПО МЕСЯЦАМ"""
    try:
        max_zn = {}
        for num in range(3, 15, 1):
            yacheika = "AW" + str(num) + ":" + "BE" + str(num)
            stroka = Read(
                Nazvanie_operazii="ЧИТАЕМ ", range=f"Счетчик посетителей!{yacheika}"
            )
            if stroka is not None:  # Исключает None строки
                # month_1 = month_dict[int(stroka[0])]
                # chel_mes = str(stroka[2])
                # pokupok_mes = str(stroka[4])
                # await message.answer(month_1+"  чел/мес :"+chel_mes+"\n покупок/мес :"+pokupok_mes)
                # print(stroka)
                """СОЗДАЕМ СЛОВАРЬ ДЛЯ НУЖНЫХ ПАРАМЕТРОВ"""
                max_zn[int(stroka[0])] = list(
                    [stroka[1], stroka[2], stroka[4], stroka[7], stroka[8]]
                )
        max_key = max_zn[
            max(max_zn, key=lambda x: float(max_zn[x][0]))
        ]  # ИЩИМ MAX ЗНАЧЕНИЕ ПО ЗАДАННОМУ МЕСТУ В СПИСКЕ (СУММА ЧЕЛОВЕК)
        keys_for_value = [
            key for key, val in max_zn.items() if val == max_key
        ]  # Поиск ключа по MAX значению
        month_1 = month_dict[int(keys_for_value[0])]  # Перевод числа в месяц
        await message.answer(
            month_1
            + ":\n СУММ ЧЕЛ :"
            + max_key[0]
            + "\n СРЕДН ЧЕЛ/МЕС :"
            + max_key[1]
            + "\n СРЕДН ПОКУПОК/МЕС :"
            + max_key[2]
            + "\n СРЕДНИЙ ЧЕК :"
            + max_key[3]
            + "\n НУЖНЫЕ ПОКУПАТЕЛИ % :"
            + max_key[4]
        )
        """ТЕКУЩЕЕ ЗНАЧЕНИЕ"""
        tekuch_znach_key, tekuch_znach_value = list(max_zn.items())[-1]
        month_2 = month_dict[int(tekuch_znach_key)]  # Перевод числа в месяц
        await message.answer(
            month_2
            + ":\n СУММ ЧЕЛ :"
            + tekuch_znach_value[0]
            + "\n СРЕДН ЧЕЛ/МЕС :"
            + tekuch_znach_value[1]
            + "\n СРЕДН ПОКУПОК/МЕС :"
            + tekuch_znach_value[2]
            + "\n СРЕДНИЙ ЧЕК :"
            + tekuch_znach_value[3]
            + "\n НУЖНЫЕ ПОКУПАТЕЛИ % :"
            + tekuch_znach_value[4]
        )
        """УСЛОВИЕ"""
        if float(tekuch_znach_value[1]) > 150:
            await message.answer("СРЕДНИЙ План по людям выполнен")
            if float(tekuch_znach_value[4]) > 80:
                await message.answer("НУЖНЫХ ПОКУПАТЕЛЕЙ ХВАТАЕТ")
                await message.answer("👍")
            else:
                await message.answer("НУЖНЫХ ПОКУПАТЕЛЕЙ НЕДОСТАТОЧНО")
                await message.answer("🤬")
        else:
            await message.answer("План по людям НЕВЫПОЛНЕН❗❗❗")
            await message.answer("ПРИВЛЕКАЙ БОЛЬШЕ ЛЮДЕЙ")
            await message.answer("😤")
        await message.answer(
            "Разберись по подробнее почему так", reply_markup=inlinebtn.poseshenie()
        )
    except:
        await message.answer("ВНЕСИ ДАННЫЕ ДЛЯ НОВОГО МЕСЯЦА❗ОШИБКА❗")


@dp.message(F.text == "ДЕЛА")
async def reply_btn(message: types.Message):
    try:
        """ИЩИМ РАНДОМНОЕ ДЕЛ"""
        vsego_del = Read2(Nazvanie_operazii="ЧИТАЕМ ", range=f"Дела и управление!J2")
        nomer_stroki = random.randint(3, int(vsego_del[0]) + int(2))
        yacheika_dela = "A" + str(nomer_stroki) + ":" + "I" + str(nomer_stroki)
        stroka_dela = Read2(
            Nazvanie_operazii="ЧИТАЕМ ", range=f"Дела и управление!{yacheika_dela}"
        )
        if stroka_dela[0] == "TRUE":
            await message.answer("ЭТО ДЕЛО СДЕЛАНО")
            await message.answer("💪")
            await message.answer(
                "СТРОКА : " + str(nomer_stroki) + "\n" + stroka_dela[4]
            )
        else:
            await message.answer(
                "СТРОКА : "
                + str(nomer_stroki)
                + "\nОКОНЧАНИЕ "
                + stroka_dela[3]
                + "\n"
                + stroka_dela[4]
                + "\nЗАВЕРШЕНО : "
                + stroka_dela[8]
            )
            """ПРЕОБРАЗУЕТ ДАТУ В НУЖНЫЙ ФОРМАТ"""
            # Словарь для соответствия русских и английских сокращений месяцев
            month_dict = {
                "янв": "Jan",
                "фев": "Feb",
                "мар": "Mar",
                "апр": "Apr",
                "май": "May",
                "июн": "Jun",
                "июл": "Jul",
                "авг": "Aug",
                "сен": "Sep",
                "окт": "Oct",
                "ноя": "Nov",
                "дек": "Dec",
            }
            # Преобразуем русское сокращение месяца в английское с помощью словаря
            for key in month_dict:
                if key in stroka_dela[3]:
                    date_slovar = stroka_dela[3].replace(key, month_dict[key])
            # Преобразование строки в объект datetime
            date_obj_delo = datetime.strptime(
                date_slovar.rstrip(".") + "." + str(datetime.now().year), "%d.%b.%Y"
            )
            """СРАВНИВАЕМ ДАТЫ"""
            now_delo = datetime.now()
            if date_obj_delo.date() < now_delo.date():
                await message.answer(
                    "ВРЕМЯ ПРОСРОЧЕНО НА :"
                    + str(date_obj_delo.date() - now_delo.date())
                )
                await message.answer("😤")
            else:
                await message.answer("ВРЕМЯ ЕЩЕ ЕСТЬ")
                await message.answer("🧠")
    except:
        pass


"""ВВОД ИДЕИ ДЛЯ ВНЕСЕНИЯ В ТАБЛИЦУ"""


@dp.message()
async def start_cmd(message: types.Message):
    plan_deistvi = [
        [
            "zzz",
            "zzz",
            "zzz",
            "zzz",
            message.text,
            "ГНОМ",
            "Улучшение",
            "С+А",
            "zzz",
            "zzz",
        ]
    ]
    Dobavlenie_vstavka_strok2(
        Nazvanie_operazii="",
        diapozon_dannich="Дела и управление!A5",
        znachenie=plan_deistvi,
    )
    await message.answer("ОТЛИЧНАЯ ИДЕЯ!Спасибо ХОЗЯИН")
    await message.answer("👍")


"""ОБРАБОТЧИК ИНЛАЙН КНОПОК"""

"""ГНОМ"""


@dp.callback_query(lambda callback_query: callback_query.data == "viruchka_GNOM")
async def process_callback_button(callback_query: types.CallbackQuery):
    global viruchk_GNOM
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="🔵🔵🔵")
    now = datetime.now().month
    if now == 1:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K3")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L3")
    elif now == 2:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K4")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L4")
    elif now == 3:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K5")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L5")
    elif now == 4:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K6")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L6")
    elif now == 5:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K7")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L7")
    elif now == 6:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K8")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L8")
    elif now == 7:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K9")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L9")
    elif now == 8:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K10")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L10")
    elif now == 9:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K11")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L11")
    elif now == 10:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K12")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L12")
    elif now == 11:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K13")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L13")
    elif now == 12:
        viruchk_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!K14")
        plan_GNOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!L14")
    else:
        pass
    GNOM_missia = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N17")
    await bot.send_message(
        callback_query.from_user.id,
        text="⚠️ МИССИЯ И ЦЕЛЬ ГНОМ ⚠️ :\n" + str(GNOM_missia[0]),
    )
    await bot.send_message(
        callback_query.from_user.id,
        text="Выручка ГНОМ : " + viruchk_GNOM[0] + " руб/мес",
    )
    if int(viruchk_GNOM[0]) < 231000:
        await bot.send_message(callback_query.from_user.id, text="БОРДОВЫЙ 🆘")
    elif int(viruchk_GNOM[0]) < 330000:
        await bot.send_message(callback_query.from_user.id, text="ТЕМНО-КРАСНЫЙ 🆘")
    elif int(viruchk_GNOM[0]) < 537000:
        await bot.send_message(callback_query.from_user.id, text="КРАСНЫЙ 🟥")
    elif int(viruchk_GNOM[0]) < 747000:
        await bot.send_message(callback_query.from_user.id, text="ЖЕЛТЫЙ 🟨")
    elif int(viruchk_GNOM[0]) < 948000:
        await bot.send_message(callback_query.from_user.id, text="ЗЕЛЕНЫЙ 🟩")
    elif int(viruchk_GNOM[0]) < 1155000:
        await bot.send_message(callback_query.from_user.id, text="СИНИЙ 🟦")
    else:
        await bot.send_message(callback_query.from_user.id, text="УРОВЕНЬ БОГ 😇")
    now = datetime.now()
    first_day_of_next_month = (now.replace(day=1) + timedelta(days=32)).replace(day=1)
    time_until_end_of_month = (first_day_of_next_month - now).days
    if int(plan_GNOM[0]) > 0:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН ГНОМ ПЕРЕВЫПОЛНЕН НА : " + str(plan_GNOM[0]) + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="До конца месяца ОСТАЛОСЬ: " + str(time_until_end_of_month) + " дн",
        )
        await bot.send_message(callback_query.from_user.id, text="ОТЛИЧНАЯ РАБОТА")
        await bot.send_message(callback_query.from_user.id, text="👍")
    else:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН ГНОМ НЕ ВЫПОЛНЕН\nНЕ ХВАТАЕТ : " + str(plan_GNOM[0]) + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="До конца месяца ОСТАЛОСЬ: " + str(time_until_end_of_month) + " дн",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="МИНИМАЛЬНАЯ выручка должна :\n"
                 + str(round(int(plan_GNOM[0]) * (-1) / time_until_end_of_month))
                 + " руб/день",
        )
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    await bot.send_message(
        callback_query.from_user.id,
        text="СДЕЛАЙ ЗАПИСЬ В\n❗ИДЕЯ❗\n Хоть самую глупую",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


"""ШАРДОМ"""


@dp.callback_query(lambda callback_query: callback_query.data == "viruchka_CHARDOM")
async def process_callback_button(callback_query: types.CallbackQuery):
    global plan, viruchk_CHARDOM
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="🔵🔵🔵")
    now = datetime.now().month
    if now == 1:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N3")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O3")
    elif now == 2:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N4")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O4")
    elif now == 3:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N5")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O5")
    elif now == 4:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N6")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O6")
    elif now == 5:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N7")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O7")
    elif now == 6:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N8")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O8")
    elif now == 7:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N9")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O9")
    elif now == 8:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N10")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O10")
    elif now == 9:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N11")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O11")
    elif now == 10:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N12")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O12")
    elif now == 11:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N13")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O13")
    elif now == 12:
        viruchk_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N14")
        plan_CHARDOM = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!O14")
    else:
        pass
    CHARDOM_missia = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N24")
    await bot.send_message(
        callback_query.from_user.id,
        text="⚠️ МИССИЯ И ЦЕЛЬ ШАРДОМ ⚠️:\n" + str(CHARDOM_missia[0]),
    )
    await bot.send_message(
        callback_query.from_user.id,
        text="Выручка ШАРДОМ : " + viruchk_CHARDOM[0] + " руб/мес",
    )
    if int(viruchk_CHARDOM[0]) < 15000:
        await bot.send_message(callback_query.from_user.id, text="БОРДОВЫЙ 🆘")
    elif int(viruchk_CHARDOM[0]) < 27000:
        await bot.send_message(callback_query.from_user.id, text="ТЕМНО-КРАСНЫЙ 🆘")
    elif int(viruchk_CHARDOM[0]) < 54000:
        await bot.send_message(callback_query.from_user.id, text="КРАСНЫЙ 🟥")
    elif int(viruchk_CHARDOM[0]) < 69000:
        await bot.send_message(callback_query.from_user.id, text="ЖЕЛТЫЙ 🟨")
    elif int(viruchk_CHARDOM[0]) < 86000:
        await bot.send_message(callback_query.from_user.id, text="ЗЕЛЕНЫЙ 🟩")
    elif int(viruchk_CHARDOM[0]) < 10000:
        await bot.send_message(callback_query.from_user.id, text="СИНИЙ 🟦")
    else:
        await bot.send_message(callback_query.from_user.id, text="УРОВЕНЬ БОГ 😇")

    now = datetime.now()
    first_day_of_next_month = (now.replace(day=1) + timedelta(days=32)).replace(day=1)
    time_until_end_of_month = (first_day_of_next_month - now).days
    if int(plan_CHARDOM[0]) > 0:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН ШАРДОМ ПЕРЕВЫПОЛНЕН НА : " + str(plan_CHARDOM[0]) + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="До конца месяца ОСТАЛОСЬ: " + str(time_until_end_of_month) + " дн",
        )
        await bot.send_message(callback_query.from_user.id, text="ОТЛИЧНАЯ РАБОТА")
        await bot.send_message(callback_query.from_user.id, text="👍")
    else:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН ШАРДОМ НЕ ВЫПОЛНЕН\nНЕ ХВАТАЕТ : "
                 + str(plan_CHARDOM[0])
                 + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="До конца месяца ОСТАЛОСЬ: " + str(time_until_end_of_month) + " дн",
        )
        await bot.send_message(
            callback_query.from_user.id,
            text="МИНИМАЛЬНАЯ выручка должна:\n "
                 + str(round(int(plan_CHARDOM[0]) * (-1) / time_until_end_of_month))
                 + " руб/день",
        )
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    await bot.send_message(
        callback_query.from_user.id,
        text="СДЕЛАЙ ЗАПИСЬ В\n❗ИДЕЯ❗\n Хоть самую глупую",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


"""МАРКЕТПЛЕЙСЫ"""


@dp.callback_query(lambda callback_query: callback_query.data == "viruchka_MARKETPLASE")
async def process_callback_button(callback_query: types.CallbackQuery):
    global plan_Marketplase, viruchka_Marketplase
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="🔵🔵🔵")
    now = datetime.now().month
    if now == 1:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R3")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S3")
    elif now == 2:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R4")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S4")
    elif now == 3:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R5")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S5")
    elif now == 4:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R6")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S6")
    elif now == 5:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R7")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S7")
    elif now == 6:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R8")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S8")
    elif now == 7:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R9")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S9")
    elif now == 8:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R10")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S10")
    elif now == 9:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R11")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S11")
    elif now == 10:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R12")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S12")
    elif now == 11:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R13")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S13")
    elif now == 12:
        viruchka_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!R14")
        plan_Marketplase = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!S14")
    else:
        pass

    Marketplase_missia = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N38")
    await bot.send_message(
        callback_query.from_user.id,
        text="⚠️ МИССИЯ И ЦЕЛЬ МАРКЕТПЛЕЙСОВ ⚠️ :\n" + str(Marketplase_missia[0]),
    )
    await bot.send_message(
        callback_query.from_user.id,
        text="ДОХОД МАРКЕТПЛЕЙСОВ :\n" + str(viruchka_Marketplase[0]) + " руб/мес",
    )
    if int(viruchka_Marketplase[0]) < 300:
        await bot.send_message(callback_query.from_user.id, text="БОРДОВЫЙ 🆘")
    elif int(viruchka_Marketplase[0]) < 600:
        await bot.send_message(callback_query.from_user.id, text="ТЕМНО-КРАСНЫЙ 🆘")
    elif int(viruchka_Marketplase[0]) < 900:
        await bot.send_message(callback_query.from_user.id, text="КРАСНЫЙ 🟥")
    elif int(viruchka_Marketplase[0]) < 1200:
        await bot.send_message(callback_query.from_user.id, text="ЖЕЛТЫЙ 🟨")
    elif int(viruchka_Marketplase[0]) < 1500:
        await bot.send_message(callback_query.from_user.id, text="ЗЕЛЕНЫЙ 🟩")
    elif int(viruchka_Marketplase[0]) < 1800:
        await bot.send_message(callback_query.from_user.id, text="СИНИЙ 🟦")
    else:
        await bot.send_message(callback_query.from_user.id, text="УРОВЕНЬ БОГ 😇")
    if int(plan_Marketplase[0]) > 0:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН МАРКЕТПЛЕЙСОВ ПЕРЕВЫПОЛНЕН НА : "
                 + str(plan_Marketplase[0])
                 + " руб",
        )
        await bot.send_message(callback_query.from_user.id, text="ОТЛИЧНАЯ РАБОТА")
        await bot.send_message(callback_query.from_user.id, text="👍")
    else:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН МАРКЕТПЛЕЙСОВ НЕ ВЫПОЛНЕН\nНЕ ХВАТАЕТ : "
                 + str(plan_Marketplase[0])
                 + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    await bot.send_message(
        callback_query.from_user.id,
        text="СДЕЛАЙ ЗАПИСЬ В\n❗ИДЕЯ❗\n Хоть самую глупую",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


"""ПАССИВНЫЙ ДОХОД"""


@dp.callback_query(lambda callback_query: callback_query.data == "passivnii_dochod")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="🔵🔵🔵")
    now = datetime.now().month
    if now == 1:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q3")
    elif now == 2:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q4")
    elif now == 3:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q5")
    elif now == 4:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q6")
    elif now == 5:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q7")
    elif now == 6:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q8")
    elif now == 7:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q9")
    elif now == 8:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q10")
    elif now == 9:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q11")
    elif now == 10:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q12")
    elif now == 11:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q13")
    elif now == 12:
        passivn_doch = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!Q14")
    else:
        pass
    passivn_doch_missia = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N31")
    await bot.send_message(
        callback_query.from_user.id,
        text="⚠️ МИССИЯ И ЦЕЛЬ ПАССИВНОГО ДОХОДА ⚠️ :\n" + str(passivn_doch_missia[0]),
    )
    await bot.send_message(
        callback_query.from_user.id,
        text="ПАССИВНЫЙ ДОХОД : " + str(passivn_doch[0]) + " руб/мес",
    )
    if int(passivn_doch[0]) < 75:
        await bot.send_message(callback_query.from_user.id, text="БОРДОВЫЙ 🆘")
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    elif int(passivn_doch[0]) < 150:
        await bot.send_message(callback_query.from_user.id, text="ТЕМНО-КРАСНЫЙ 🆘")
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    elif int(passivn_doch[0]) < 300:
        await bot.send_message(callback_query.from_user.id, text="КРАСНЫЙ 🟥")
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    elif int(passivn_doch[0]) < 500:
        await bot.send_message(callback_query.from_user.id, text="ЖЕЛТЫЙ 🟨")
    elif int(passivn_doch[0]) < 750:
        await bot.send_message(callback_query.from_user.id, text="ЗЕЛЕНЫЙ 🟩")
    elif int(passivn_doch[0]) < 1000:
        await bot.send_message(callback_query.from_user.id, text="СИНИЙ 🟦")
    else:
        await bot.send_message(callback_query.from_user.id, text="УРОВЕНЬ БОГ 😇")
    await bot.send_message(
        callback_query.from_user.id,
        text="СДЕЛАЙ ЗАПИСЬ В\n❗ИДЕЯ❗\n Хоть самую глупую",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


"""КОРПОРАЦИЯ РОБОТОВ"""


@dp.callback_query(lambda callback_query: callback_query.data == "korporazia_robotov")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="🔵🔵🔵")
    now = datetime.now().month
    if now == 1:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U3")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V3")
    elif now == 2:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U4")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V4")
    elif now == 3:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U5")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V5")
    elif now == 4:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U6")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V6")
    elif now == 5:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U7")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V7")
    elif now == 6:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U8")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V8")
    elif now == 7:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U9")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V9")
    elif now == 8:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U10")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V10")
    elif now == 9:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U11")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V11")
    elif now == 10:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U12")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V12")
    elif now == 11:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U13")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V13")
    elif now == 12:
        korporaz_robot = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!U14")
        korporaz_robot_plan = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!V14")
    else:
        pass
    korporaz_robot_missia = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!N45")
    await bot.send_message(
        callback_query.from_user.id,
        text="⚠️ МИССИЯ И ЦЕЛЬ КОРПОРАЦИИ РОБОТОВ ⚠️ :\n" + str(korporaz_robot_missia[0]),
    )
    await bot.send_message(
        callback_query.from_user.id,
        text="ДОХОД КОРПОРАЦИИ РОБОТОВ : " + str(korporaz_robot[0]) + " руб/мес",
    )
    if int(korporaz_robot[0]) < 300:
        await bot.send_message(callback_query.from_user.id, text="БОРДОВЫЙ 🆘")
    elif int(korporaz_robot[0]) < 600:
        await bot.send_message(callback_query.from_user.id, text="ТЕМНО-КРАСНЫЙ 🆘")
    elif int(korporaz_robot[0]) < 900:
        await bot.send_message(callback_query.from_user.id, text="КРАСНЫЙ 🟥")
    elif int(korporaz_robot[0]) < 1200:
        await bot.send_message(callback_query.from_user.id, text="ЖЕЛТЫЙ 🟨")
    elif int(korporaz_robot[0]) < 1500:
        await bot.send_message(callback_query.from_user.id, text="ЗЕЛЕНЫЙ 🟩")
    elif int(korporaz_robot[0]) < 1800:
        await bot.send_message(callback_query.from_user.id, text="СИНИЙ 🟦")
    else:
        await bot.send_message(callback_query.from_user.id, text="УРОВЕНЬ БОГ 😇")
    if int(korporaz_robot_plan[0]) > 0:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН В КОРПОРАЦИИ РОБОТОВ ПЕРЕВЫПОЛНЕН НА : "
                 + str(korporaz_robot_plan[0])
                 + " руб",
        )
        await bot.send_message(callback_query.from_user.id, text="ОТЛИЧНАЯ РАБОТА")
        await bot.send_message(callback_query.from_user.id, text="👍")
    else:
        await bot.send_message(
            callback_query.from_user.id,
            text="ПЛАН В КОРПОРАЦИИ РОБОТОВ НЕ ВЫПОЛНЕН\nНЕ ХВАТАЕТ : "
                 + str(korporaz_robot_plan[0])
                 + " руб",
        )
        await bot.send_message(
            callback_query.from_user.id, text="ДУМАЙ ПОЛУЧШЕ\nКАК ЭТО ИСПРАВИТЬ❓"
        )
        await bot.send_message(
            callback_query.from_user.id, text="ЧТО МОЖНО СДЕЛАТЬ ДЛЯ ЭТОГО?"
        )
        await bot.send_message(callback_query.from_user.id, text="🤔")
    await bot.send_message(
        callback_query.from_user.id,
        text="СДЕЛАЙ ЗАПИСЬ В\n❗ИДЕЯ❗\n Хоть самую глупую",
        reply_markup=inlinebtn.get_inline_keyboard(),
    )


"""ВЫВОД О ПОГОДЕ"""


@dp.callback_query(lambda callback_query: callback_query.data == "result_day")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # vivod = Read(Nazvanie_operazii="ЧИТАЕМ ", range="Данные!AD54")
    await bot.send_message(callback_query.from_user.id, text="Сдесь текст результатов за день")


"""ПОСЕЩЕНИЕ ПОДРОБНО"""


@dp.callback_query(lambda callback_query: callback_query.data == "posesheni")
async def process_callback_button(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text="ЖДИТЕ")
    vse_zn = {}
    for num in range(3, 15, 1):
        yacheika = "AW" + str(num) + ":" + "BE" + str(num)
        stroka_vse = Read(
            Nazvanie_operazii="ЧИТАЕМ ", range=f"Счетчик посетителей!{yacheika}"
        )
        if stroka_vse is not None:  # Исключает None строки
            # month_1 = month_dict[int(stroka[0])]
            # chel_mes = str(stroka[2])
            # pokupok_mes = str(stroka[4])
            # await message.answer(month_1+"  чел/мес :"+chel_mes+"\n покупок/мес :"+pokupok_mes)
            # print(stroka)
            """СОЗДАЕМ СЛОВАРЬ ДЛЯ НУЖНЫХ ПАРАМЕТРОВ"""
            vse_zn[int(stroka_vse[0])] = list(
                [
                    stroka_vse[1],
                    stroka_vse[2],
                    stroka_vse[4],
                    stroka_vse[7],
                    stroka_vse[8],
                ]
            )
    for key_vse, value_vse in vse_zn.items():
        # print("Ключ:", key)
        month_3 = month_dict[int(key_vse)]
        # print("Значение:", value)
        # print("-------------------")
        await bot.send_message(
            callback_query.from_user.id,
            text=month_3
                 + ":\n СУММ ЧЕЛ :"
                 + value_vse[0]
                 + "\n СРЕДН ЧЕЛ/МЕС :"
                 + value_vse[1]
                 + "\n СРЕДН ПОКУПОК/МЕС :"
                 + value_vse[2]
                 + "\n СРЕДНИЙ ЧЕК :"
                 + value_vse[3]
                 + "\n НУЖНЫЕ ПОКУПАТЕЛИ % :"
                 + value_vse[4],
        )

    # max_key = max_zn[
    #     max(max_zn, key=lambda x: float(max_zn[x][0]))]  # ИЩИМ MAX ЗНАЧЕНИЕ ПО ЗАДАННОМУ МЕСТУ В СПИСКЕ (СУММА ЧЕЛОВЕК)
    # keys_for_value = [key for key, val in max_zn.items() if val == max_key]  # Поиск ключа по MAX значению
    # month_1 = month_dict[int(keys_for_value[0])]  # Перевод числа в месяц


"""ДИСПЕТЧЕР ПОСТОЯННО СЛУШАЕТ"""


async def main():
    await dp.start_polling(bot)
    await bot.set_my_commands(commands=[], scope=types.BotCommandScopeAllPrivateChats())


"""ЗАПУСТИЛИ МАЙН"""
asyncio.run(main())
