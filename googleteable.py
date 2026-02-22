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

#   ----------------НАЧАЛО КОНСТАНТЫ БИЗНЕС ЛОГИКИ-------------------------
# Маппинг месяца → буква столбца в Google Таблице (январь = B, февраль = C, ...)
MONTH_TO_COLUMN = {1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M"}
DATA_TO_MONTH = {"2026-01": 2, "2026-02": 3, "2026-03": 4, "2026-04": 5, "2026-05": 6, "2026-06": 7, "2026-07": 8,
                 "2026-08": 9, "2026-09": 10, "2026-10": 11, "2026-11": 12, "2026-12": 13}
# SAMPLE_RANGE_NAME = "Как продавать на 77000!A1:E250"  # НАЗВАНИЕ ЛИСТА И ДИАПОЗОН
load_dotenv(".env.wallet")
spreadsheet = os.getenv("spreadsheet")


class GoogleSheet:
    SPREADSHEET_ID = spreadsheet  # АЙ ДИ ТАБЛИЦИ
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

    def updateRangeValues(self, range, values):
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
            includeValuesInResponse="true",
            # true-включена информация о добавленных строках после операции
            # false-содержит только информацию о добавленных строках без значений ячеек
            responseValueRenderOption="FORMATTED_VALUE",
            # FORMATTED_VALUE-Значения будут рассчитаны и отформатированы в ответе в соответствии с форматированием ячейки
            # UNFORMATTED_VALUE-Значения будут рассчитаны, но не отформатированы в ответе
            # FORMULA - Значения не будут рассчитаны. Ответ будет включать формулы
            body=body,
        ).execute()

    def updateRangeValues_Picture(self, range, values):
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

    def appendRangeValues(self, range, values):
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

    def appendRangeValues_vstavka_strok(self, range, values):
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

    def ReadTable(self, range):
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

    def ReadTable_colums(self, range):
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

    def Delete(self, range):
        """УДАЛЕНИЕ В ЗАДАННОМ ДИАПАЗОНЕ (СВ-ВО В ЗАДАННОМ ДИАПАЗОНЕ ОСТАЕТСЯ)"""
        self.service.spreadsheets().values().clear(
            spreadsheetId=self.SPREADSHEET_ID, range=range
        ).execute()

    def _get_sheet_id(self, sheet_name: str) -> int:
        """Получает числовой ID листа по его названию"""
        spreadsheet_data = self.service.spreadsheets().get(
            spreadsheetId=self.SPREADSHEET_ID
        ).execute()

        for sheet in spreadsheet_data.get("sheets", []):
            if sheet["properties"]["title"] == sheet_name:
                return sheet["properties"]["sheetId"]

        raise ValueError(f"❌ Лист '{sheet_name}' не найден в таблице")

    def delete_row(self, sheet_name: str, row_index: int):
        """Удаляет всю строку из Google Таблицы.
        :param sheet_name: Название листа (например, "Лист1")
        :param row_index: Номер строки (1-based, т.е. первая строка = 1)"""
        sheet_id = self._get_sheet_id(sheet_name)
        body = {
            "requests": [
                {
                    "deleteDimension": {
                        "range": {
                            "sheetId": sheet_id,
                            "dimension": "ROWS",
                            "startIndex": row_index - 1,  # API использует 0-based индекс
                            "endIndex": row_index  # endIndex не включается
                        }
                    }
                }
            ]
        }
        self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.SPREADSHEET_ID,
            body=body
        ).execute()


"""___________________КОНЕЦ_______________________"""

"""__________НАЧАЛО ФУНКЦИЙ__________"""

"""Перезапись ячеек"""


def Izmenenie(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ИЗМЕНЕНИЕ (ЗАМЕНА) ЯЧЕЕК"""
    GoogleSheet().updateRangeValues(range=diapozon_dannich, values=znachenie)
    # НАЗВАНИЕ ЛИСТА!КЛЕТКА С КОТОРОЙ
    # ВСЕ НАЧНЕТСЯ :ГДЕ ПРЕДПОЛОГАЕМО ЗАКОНЧИТСЯ


"""Добавление ячеек"""


def Dobavlenie(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК НА СВОБОДНОМ МЕСТЕ"""
    GoogleSheet().appendRangeValues(range=diapozon_dannich, values=znachenie)


def Dobavlenie_vstavka_strok(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК СО ВСТАВКОЙ СТРОК"""
    GoogleSheet().appendRangeValues_vstavka_strok(
        range=diapozon_dannich, values=znachenie
    )


def Read(Nazvanie_operazii, range):
    """ЧТЕНИЕ 1 СТРОКИ В УКАЗАННОМ ДИАПАЗОНЕ (БЕЗ ПУСТЫХ ЯЧЕЕК)"""
    values = GoogleSheet().ReadTable(range=range).get("values", [])
    # return values
    if not values:
        return
    else:
        for row in values:
            return row


def Read_massiv_stroki(Nazvanie_operazii, range):
    """ЧТЕНИЕ СТРОК ПОЛНОСТЬЮ ДИАПАЗОН C ПУСТЫМИ ЯЧЕЙКАМИ ВНУТРИ (ЕСЛИ ВНЕШНИЕ ЯЧЕЙКИ ПУСТЫЕ ИХ НЕ БЕРЕТ)"""
    values = GoogleSheet().ReadTable(range=range).get("values", [])
    return values


def Read_massiv_colums(Nazvanie_operazii, range):
    """ЧТЕНИЕ КОЛОНН ПОЛНОСТЬЮ ДИАПАЗОН C ПУСТЫМИ ЯЧЕЙКАМИ ВНУТРИ (ЕСЛИ ВНЕШНИЕ ЯЧЕЙКИ ПУСТЫЕ ИХ НЕ БЕРЕТ)"""
    values = GoogleSheet().ReadTable_colums(range=range).get("values", [])
    return values


def Delete_diapoz(diapozon_dannich):
    """УДАЛЕНИЕ В ЗАДАННОМ ДИАПАЗОНЕ (СВ-ВО В ЗАДАННОМ ДИАПАЗОНЕ ОСТАЕТСЯ)"""
    GoogleSheet().Delete(range=diapozon_dannich)


def Delete_row(sheet_name, row_index):
    """Удаляет всю строку из Google Таблицы."""
    GoogleSheet().delete_row(sheet_name, row_index)


if __name__ == "__main__":
    pass
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
