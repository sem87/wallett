import os.path
import pickle
from dotenv import find_dotenv, load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# import pyautogui
# import base64
# from io import BytesIO
# from PIL import Image


# SAMPLE_RANGE_NAME = "Как продавать на 77000!A1:E250"  # НАЗВАНИЕ ЛИСТА И ДИАПОЗОН
load_dotenv(".env.wallet")
spreadsheet2 = os.getenv("spreadsheet2")

class GoogleSheet:
    SPREADSHEET_ID = spreadsheet2
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]  # ЧТОБЫ ЧИТАТЬ И ЗАПИСЫВАТЬ
    service = None

    def __init__(self):
        """ИШИТ ТОКЕН,И ЕСЛИ НЕ НАХОДИТ ТО ПЫТАЕТСЯ СОЗДАТЬ ЧЕРЕЗ РЕГИСТРАЦИЮ,В ПИКЛ"""
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            """ЕСЛИ НЕТ ПИКЛ КРЕДС ТО МЫ ЕГО СОЗДАЕМ"""
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print("СОЗДАЕМ КРЕДС ПОТОМУ ЧТО ЕГО НЕ ОКАЗАЛОСЬ")
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)

        self.service = build(
            "sheets", "v4", credentials=creds
        )  # ПЕРЕДАЕМ ВСЕ ДАННЫЕ О НАШЕЙ ТАБЛИЦЕ

    """ОСНОВНЫЕ ФУНКЦИИ ЗАМЕНЫ ЯЧЕЕК"""

    """ФУНКЦИИ ПЕРЕЗАПИСИ ЯЧЕЕК"""

    def updateRangeValues2(self, range, values):
        """КЛАСС ИЗМЕНЕНИЕ (ЗАМЕНА) ЯЧЕЕК"""
        body = {"values": values}
        self.service.spreadsheets().values().update(
            spreadsheetId=self.SPREADSHEET_ID,
            # ID самой книги гугл таблици
            range=range,
            # диапазон 'лист!ячейки'
            valueInputOption="USER_ENTERED",
            # valueInputOption - КАК следует интерпретировать входные данные,
            # (RAW - значения не будут анализироваться и будут сохранены как есть);
            # (USER_ENTERED как пользователь вводит со всеми кнопками)
            # includeValuesInResponse="true",
            # true-включена информация о добавленных строках после операции
            # false-содержит только информацию о добавленных строках без значений ячеек
            # responseValueRenderOption='FORMATTED_VALUE',
            # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
            # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
            # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
            body=body,
        ).execute()

    def updateRangeValues_Picture2(self, range, values):
        """КЛАСС ИЗМЕНЕНИЕ (ЗАМЕНА) ЯЧЕЕК"""
        body = {"values": ['=IMAGE("' + "image_url" + '")']}
        self.service.spreadsheets().values().update(
            spreadsheetId=self.SPREADSHEET_ID,
            # ID самой книги гугл таблици
            range=range,
            # диапазон 'лист!ячейки'
            valueInputOption="RAW",
            # valueInputOption - КАК следует интерпретировать входные данные,
            # (RAW - значения не будут анализироваться и будут сохранены как есть);
            # (USER_ENTERED как пользователь вводит со всеми кнопками)
            # includeValuesInResponse="true",
            # true-включена информация о добавленных строках после операции
            # false-содержит только информацию о добавленных строках без значений ячеек
            # responseValueRenderOption='FORMATTED_VALUE',
            # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
            # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
            # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
            body=body,
        ).execute()
        """___________________КОНЕЦ_______________________"""

    """ФУНКЦИИ ДОБАВЛЕНИЯ ЯЧЕЕК В КОНЕЦ УКАЗАННОГО ДИАПОЗОНА"""

    def appendRangeValues2(self, range, values):
        """КЛАСС ДОБАВЛЯЕТ ЗНАЧЕНИЕ ЯЧЕЕК В КОНЕЦ УКАЗАННОГО ДИАПАЗОНА"""
        body = {"values": values}
        self.service.spreadsheets().values().append(
            spreadsheetId=self.SPREADSHEET_ID,
            # ID самой книги гугл таблици
            range=range,
            # диапазон 'лист!ячейки'
            valueInputOption="USER_ENTERED",
            # valueInputOption - КАК следует интерпретировать входные данные,
            # (RAW - значения не будут анализироваться и будут сохранены как есть);
            # (USER_ENTERED как пользователь вводит со всеми кнопками)
            insertDataOption="OVERWRITE",
            # INSERT_ROWS Строки вставляются для новых данных
            # OVERWRITE Без добавления ,но если нет строк то добавляет
            includeValuesInResponse="true",
            # true-включена информация о добавленных строках после операции
            # false-содержит только информацию о добавленных строках без значений ячеек
            responseValueRenderOption="FORMATTED_VALUE",
            # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
            # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
            # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
            # responseDateTimeRenderOption='SERIAL_NUMBER',
            # SERIAL_NUMBER-Указывает, что поля даты, времени, даты и времени должны выводиться как числа двойной точности в формате «порядковый номер»
            # FORMATTED_STRING-Указывает, что поля даты, времени, даты и времени и продолжительности должны выводиться в виде строк в заданном числовом формате
            body=body,
        ).execute()
        # values() используется со словарями и возвращает представление всех значений в словаре
        # execute() передает до гугл таблиц это завершение процесса

    def appendRangeValues_vstavka_strok2(self, range, values):
        """КЛАСС ДОБАВЛЯЕТ ЗНАЧЕНИЕ ЯЧЕЕК ОДНОВРЕМЕННО СО ВСТАВКОЙ СТРОК"""
        body = {"values": values}
        self.service.spreadsheets().values().append(
            spreadsheetId=self.SPREADSHEET_ID,
            # ID самой книги гугл таблици
            range=range,
            # диапазон 'лист!ячейки'
            valueInputOption="USER_ENTERED",
            # valueInputOption - КАК следует интерпретировать входные данные,
            # (RAW - значения не будут анализироваться и будут сохранены как есть);
            # (USER_ENTERED как пользователь вводит со всеми кнопками)
            insertDataOption="INSERT_ROWS",
            # INSERT_ROWS Строки вставляются для новых данных
            # OVERWRITE Без добавления ,но если нет строк то добавляет
            includeValuesInResponse="true",
            # true-включена информация о добавленных строках после операции
            # false-содержит только информацию о добавленных строках без значений ячеек
            responseValueRenderOption="FORMATTED_VALUE",
            # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
            # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
            # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
            # responseDateTimeRenderOption='SERIAL_NUMBER',
            # SERIAL_NUMBER-Указывает, что поля даты, времени, даты и времени должны выводиться как числа двойной точности в формате «порядковый номер»
            # FORMATTED_STRING-Указывает, что поля даты, времени, даты и времени и продолжительности должны выводиться в виде строк в заданном числовом формате
            body=body,
        ).execute()
        # values() используется со словарями и возвращает представление всех значений в словаре
        # execute() передает до гугл таблиц это завершение процесса

        """___________________КОНЕЦ_______________________"""

    """ФУНКЦИИ ЧТЕНИЯ ЯЧЕЕК"""

    def ReadTable2(self, range):
        """КЛАСС ЧТЕНИЕ ЯЧЕЕК В ЗАДАННОМ ДИАПАЗОНЕ"""
        result = (
            self.service.spreadsheets()
            .values()
            .get(
                spreadsheetId=self.SPREADSHEET_ID,
                # majorDimension = "COLUMNS",
                # ROWS-Работает со строками листа.
                # COLUMNS-Работает со столбцами листа.
                # valueRenderOption = "FORMATTED_VALUE",
                # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
                # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
                # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
                # dateTimeRenderOption = "",
                # SERIAL_NUMBER-Указывает, что поля даты, времени, даты и времени должны выводиться как числа двойной точности в формате «порядковый номер»
                # FORMATTED_STRING-Указывает, что поля даты, времени, даты и времени и продолжительности должны выводиться в виде строк в заданном числовом формате
                range=range,
            )
            .execute()
        )
        return result

    def ReadTable_colums2(self, range):
        """КЛАСС ЧТЕНИЕ КОЛОНН В ЗАДАННОМ ДИАПАЗОНЕ"""
        result = (
            self.service.spreadsheets()
            .values()
            .get(
                spreadsheetId=self.SPREADSHEET_ID,
                majorDimension="COLUMNS",
                # ROWS-Работает со строками листа.
                # COLUMNS-Работает со столбцами листа.
                # valueRenderOption = "FORMATTED_VALUE",
                # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
                # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
                # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
                # dateTimeRenderOption = "",
                # SERIAL_NUMBER-Указывает, что поля даты, времени, даты и времени должны выводиться как числа двойной точности в формате «порядковый номер»
                # FORMATTED_STRING-Указывает, что поля даты, времени, даты и времени и продолжительности должны выводиться в виде строк в заданном числовом формате
                range=range,
            )
            .execute()
        )
        return result

    """ ___________________КОНЕЦ_______________________ """

    """ФУНКЦИИ УДАЛЕНИЯ ЯЧЕЕК"""

    def Delete2(self, range):
        """УДАЛЕНИЕ В ЗАДАННОМ ДИАПАЗОНЕ (СВ-ВО В ЗАДАННОМ ДИАПАЗОНЕ ОСТАЕТСЯ)"""
        self.service.spreadsheets().values().clear(
            spreadsheetId=self.SPREADSHEET_ID, range=range
        ).execute()


"""___________________КОНЕЦ_______________________"""

"""__________НАЧАЛО ФУНКЦИЙ__________"""

"""Перезапись ячеек"""


def Izmenenie2(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ИЗМЕНЕНИЕ (ЗАМЕНА) ЯЧЕЕК"""
    GoogleSheet().updateRangeValues2(range=diapozon_dannich, values=znachenie)
    # НАЗВАНИЕ ЛИСТА!КЛЕТКА С КОТОРОЙ
    # ВСЕ НАЧНЕТСЯ :ГДЕ ПРЕДПОЛОГАЕМО ЗАКОНЧИТСЯ


"""Добавление ячеек"""


def Dobavlenie2(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК НА СВОБОДНОМ МЕСТЕ"""
    GoogleSheet().appendRangeValues2(range=diapozon_dannich, values=znachenie)


def Dobavlenie_vstavka_strok2(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК СО ВСТАВКОЙ СТРОК"""
    GoogleSheet().appendRangeValues_vstavka_strok2(
        range=diapozon_dannich, values=znachenie
    )


def Read2(Nazvanie_operazii, range):
    """ЧТЕНИЕ 1 СТРОКИ В УКАЗАННОМ ДИАПАЗОНЕ (БЕЗ ПУСТЫХ ЯЧЕЕК)"""
    values = GoogleSheet().ReadTable2(range=range).get("values", [])
    # return values
    if not values:
        return
    else:
        for row in values:
            return row


def Read_massiv_stroki2(Nazvanie_operazii, range):
    """ЧТЕНИЕ СТРОК ПОЛНОСТЬЮ ДИАПАЗОН C ПУСТЫМИ ЯЧЕЙКАМИ ВНУТРИ (ЕСЛИ ВНЕШНИЕ ЯЧЕЙКИ ПУСТЫЕ ИХ НЕ БЕРЕТ)"""
    values = GoogleSheet().ReadTable2(range=range).get("values", [])
    return values


def Read_massiv_colums2(Nazvanie_operazii, range):
    """ЧТЕНИЕ КОЛОНН ПОЛНОСТЬЮ ДИАПАЗОН C ПУСТЫМИ ЯЧЕЙКАМИ ВНУТРИ (ЕСЛИ ВНЕШНИЕ ЯЧЕЙКИ ПУСТЫЕ ИХ НЕ БЕРЕТ)"""
    values = GoogleSheet().ReadTable_colums2(range=range).get("values", [])
    return values


def Delete_diapoz2(diapozon_dannich):
    """УДАЛЕНИЕ В ЗАДАННОМ ДИАПАЗОНЕ (СВ-ВО В ЗАДАННОМ ДИАПАЗОНЕ ОСТАЕТСЯ)"""
    GoogleSheet().Delete2(range=diapozon_dannich)


if __name__ == "__main__":
    pass
    # Izmenenie2(Nazvanie_operazii='q', diapozon_dannich=f'АНАЛИЗ ОЗОН!D11', znachenie=[[777]])
    # spgoogle = [["ПРОВЕРКА"],["ГУГЛА"]]
    # Dobavlenie2(Nazvanie_operazii='ДОБАВЛЯЕМ В ТАБЛИЦУ', diapozon_dannich='ВАТСАП КОНТРОЛЬ!C2:C',
    #             znachenie=spgoogle)
    # prodazi = [['=D1+E1', 'zzz'], ['zzz', 'zzz']]
    # b = Read(Nazvanie_operazii='', range="ПРОБНЫЙ!B:D6")
    # a = Read_massiv_colums(Nazvanie_operazii='', range="ПРОБНЫЙ!B2:D7")
    # print(a)
    # Delete_diapoz(diapozon_dannich='ПРОБНЫЙ!A2:M')

# Izmenenie(Nazvanie_operazii='ВВОД ПРОДАЖИ : ', diapozon_dannich='Лист2!A1:F', znachenie=prodazi)
# Read(Nazvanie_operazii='ЧИТАЕМ ', range="Лист2!A1:F")
# Dobavlenie(Nazvanie_operazii='ДОБАВИМ ЯЧЕЙКИ', diapozon_dannich='Лист2!A1:K', znachenie=pi)

# НА ВСЯКИЙ СЛУЧАЙ
# spreadsheets.create: Создает новую таблицу.
# spreadsheets.get: Получает метаданные таблицы.
# spreadsheets.values.get: Получает значения из определенного диапазона ячеек в таблице.
# spreadsheets.values.update: Обновляет значения в определенном диапазоне ячеек в таблице.
# spreadsheets.values.append: Добавляет значения в конец определенного диапазона ячеек в таблице.
# spreadsheets.batchUpdate: Запускает несколько обновлений в таблице параллельно для оптимизации производительности.
