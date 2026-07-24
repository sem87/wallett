import os.path
import pickle
from dotenv import find_dotenv, load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

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
if os.path.exists(".env.wallet"):
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
        response = self.service.spreadsheets().values().append(
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
        # Возвращаем ответ API (там содержится информация о том, куда именно вставилось)
        return response

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

    def get_next_empty_row(self, sheet_name):
        """Возвращает номер первой пустой строки на листе"""
        # Считываем весь столбец A, чтобы найти последнюю заполненную строку
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.SPREADSHEET_ID,
            range=f"{sheet_name}!A:A"
        ).execute()

        values = result.get('values', [])
        # Если таблица полностью пустая, начинаем с 1-й строки.
        # Иначе длина массива + 1 (можно изменить на +2, если есть шапка)
        return len(values) + 1 if len(values) > 0 else 1


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


# def Dobavlenie_vstavka_strok(Nazvanie_operazii, diapozon_dannich, znachenie):
#     """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК СО ВСТАВКОЙ СТРОК"""
#     GoogleSheet().appendRangeValues_vstavka_strok(
#         range=diapozon_dannich, values=znachenie
#     )


def Dobavlenie_vstavka_strok(Nazvanie_operazii, diapozon_dannich, znachenie):
    """ДОБАВЛЕНИЕ ЗАДАННЫХ ЯЧЕЕК СО ВСТАВКОЙ СТРОК С ДИНАМИЧЕСКОЙ ФОРМУЛОЙ"""

    # 1. Извлекаем имя листа из диапазона (например, из "Дела и управление!A5" получаем "Дела и управление")
    sheet_name = diapozon_dannich.split('!')[0]

    # 2. Узнаем номер первой пустой строки
    gs = GoogleSheet()
    target_row = gs.get_next_empty_row(sheet_name)

    # 3. Проходимся по всем строкам, которые мы хотим вставить (обычно это 1 строка, но делаем универсально)
    for i, row_data in enumerate(znachenie):
        current_row = target_row + i
        # ==================НАЧАЛО ДЕЛА И УПРАВЛЕНИЕ=====================
        # Проверяем, есть ли у нас маркер для формулы в 4-м столбце (индекс 3, это столбец D)
        # Замените "FORMULA_HERE" на то, что вы решите использовать как маркер,
        # или просто формируйте формулу сразу при создании action_plan (см. ниже)
        if len(row_data) > 3 and isinstance(row_data[3], str) and "FORMULA" in row_data[3]:
            # Формируем формулу: =$B{номер_строки}+C{номер_строки}-1
            # Знак $ перед B фиксирует столбец B при копировании, C остается относительным
            row_data[3] = f"=$B{current_row}+C{current_row}-1"

            # --- ОБРАБОТКА СТОЛБЦА L (Индекс 11) ---
        if len(row_data) > 11 and row_data[11] == "SPARK":
            # ВАЖНО: {{ и }} используются, чтобы Python не пытался прочитать их как переменные f-строки.
            # Они превратятся в одиночные { и } при отправке в Google Таблицу.
            row_data[11] = f'=ЕСЛИОШИБКА(SPARKLINE(K{current_row},{{"charttype","bar";"color1","black";"max",1}}))'
        # ==================КОНЕЦ ДЕЛА И УПРАВЛЕНИЕ=====================
        # ==================НАЧАЛО МОЛНИЯ=====================
        # --- ОБРАБОТКА СТОЛБЦА Z (Индекс 25) ---
        if len(row_data) > 25 and isinstance(row_data[25], str) and "COST_PLECHO" in row_data[25]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[25] = (
                f"=ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=5000;0;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=50000;40;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=100000;75;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=250000;180;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=500000;350;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=1000000;700;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=2500000;1750;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=5000000;3500;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=10000000;6900;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=25000000;(F{current_row}*E{current_row})*AF{current_row}*0,68;"
                f"ЕСЛИ((F{current_row}*E{current_row})*AF{current_row}<=50000000;(F{current_row}*E{current_row})*AF{current_row}*0,65;"
                f"(F{current_row}*E{current_row})*AF{current_row}*0,57)))))))))))"
            )

        # --- ОБРАБОТКА СТОЛБЦА AA (Индекс 26) ---
        if len(row_data) > 26 and isinstance(row_data[26], str) and "ITOGO_1" in row_data[26]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[26] = (f'=ЕСЛИ(C{current_row}="покупка",'f'ЕСЛИ(T{current_row}="",0,'
                            f'(T{current_row}*U{current_row}-T{current_row}*U{current_row}*0.0005-'
                            f'ЕСЛИ(F{current_row}<T{current_row},(T{current_row}*U{current_row}-F{current_row}*U{current_row})*0.13,0)'
                            f'-(F{current_row}*U{current_row}+F{current_row}*U{current_row}*0.0005))),'
                            f'ЕСЛИ(T{current_row}="",0,'
                            f'((F{current_row}*U{current_row}-F{current_row}*U{current_row}*0.0005)'
                            f'-(T{current_row}*U{current_row}+T{current_row}*U{current_row}*0.0005)'
                            f'-ЕСЛИ(T{current_row}<F{current_row},(F{current_row}*U{current_row}-T{current_row}*U{current_row})*0.13,0))))'
                            )

        # --- ОБРАБОТКА СТОЛБЦА AB (Индекс 27) ---
        if len(row_data) > 27 and isinstance(row_data[27], str) and "ITOGO_2" in row_data[27]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[27] = (f'=ЕСЛИ(C{current_row}="покупка",'f'ЕСЛИ(V{current_row}="",0,'
                            f'(V{current_row}*W{current_row}-V{current_row}*W{current_row}*0.0005-'
                            f'ЕСЛИ(F{current_row}<V{current_row},(V{current_row}*W{current_row}-F{current_row}*W{current_row})*0.13,0)'
                            f'-(F{current_row}*W{current_row}+F{current_row}*W{current_row}*0.0005))),'
                            f'ЕСЛИ(V{current_row}="",0,'
                            f'((F{current_row}*W{current_row}-F{current_row}*W{current_row}*0.0005)'
                            f'-(V{current_row}*W{current_row}+V{current_row}*W{current_row}*0.0005)'
                            f'-ЕСЛИ(V{current_row}<F{current_row},(F{current_row}*W{current_row}-V{current_row}*W{current_row})*0.13,0))))'
                            )

        # --- ОБРАБОТКА СТОЛБЦА AC (Индекс 28) ---
        if len(row_data) > 28 and isinstance(row_data[28], str) and "ITOGO_3" in row_data[28]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[28] = (f'=ЕСЛИ(C{current_row}="покупка",'f'ЕСЛИ(X{current_row}="",0,'
                            f'(X{current_row}*Y{current_row}-X{current_row}*Y{current_row}*0.0005-'
                            f'ЕСЛИ(F{current_row}<X{current_row},(X{current_row}*Y{current_row}-F{current_row}*Y{current_row})*0.13,0)'
                            f'-(F{current_row}*Y{current_row}+F{current_row}*Y{current_row}*0.0005))),'
                            f'ЕСЛИ(X{current_row}="",0,'
                            f'((F{current_row}*Y{current_row}-F{current_row}*Y{current_row}*0.0005)'
                            f'-(X{current_row}*Y{current_row}+X{current_row}*Y{current_row}*0.0005)'
                            f'-ЕСЛИ(X{current_row}<F{current_row},(F{current_row}*Y{current_row}-X{current_row}*Y{current_row})*0.13,0))))'
                            )

        # --- ОБРАБОТКА СТОЛБЦА AD (Индекс 29) ---
        if len(row_data) > 29 and isinstance(row_data[29], str) and "ITOGO" in row_data[29]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[29] = (
                f'=ЕСЛИ(E{current_row}<U{current_row}+W{current_row}+Y{current_row},"ошибка кол-ва",'f'(ЕСЛИ(T{current_row}="",0,AA{current_row})'
                f'+ЕСЛИ(V{current_row}="",0,AB{current_row})'
                f'+ЕСЛИ(X{current_row}="",0,AC{current_row})'
                f'-Z{current_row}))'
            )
        # --- ОБРАБОТКА СТОЛБЦА AE (Индекс 30) ---
        if len(row_data) > 30 and isinstance(row_data[30], str) and "PREDBEZYBITOK" in row_data[30]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[30] = (
                f'=ЕСЛИОШИБКА(ЕСЛИ(AD{current_row}="ошибка кол-ва","ошибка кол-ва",'f'ЕСЛИ(C{current_row}="покупка",'
                f'(F{current_row}*(U{current_row}+W{current_row}+Y{current_row})-AD{current_row})*1.00093/(U{current_row}+W{current_row}+Y{current_row}),'
                f'(F{current_row}*(U{current_row}+W{current_row}+Y{current_row})+AD{current_row})*1.00093/(U{current_row}+W{current_row}+Y{current_row}))))'
            )
        # --- ОБРАБОТКА СТОЛБЦА AF (Индекс 31) ---
        if len(row_data) > 31 and isinstance(row_data[31], str) and "DNEY" in row_data[31]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[31] = f"=AH{current_row}-D{current_row}"

        # --- ОБРАБОТКА СТОЛБЦА AG (Индекс 32) ---
        if len(row_data) > 32 and isinstance(row_data[32], str) and "PROZENT" in row_data[32]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[32] = f"=ЕСЛИОШИБКА((AD{current_row}/(E{current_row}*F{current_row}))*100)"

        # --- ОБРАБОТКА СТОЛБЦА AH (Индекс 33) --- это дата
        # --- ОБРАБОТКА СТОЛБЦА AI (Индекс 34) ---
        if len(row_data) > 34 and isinstance(row_data[34], str) and "REZULTAT" in row_data[34]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[34] = (
                f'=ЕСЛИ(AD{current_row}="ошибка кол-ва","ошибка кол-ва",'f'ЕСЛИ(E{current_row}>U{current_row}+W{current_row}+Y{current_row},"процес",'
                f'ЕСЛИ(AD{current_row}>0,"заработок","убыток")))'
            )

        # # --- ОБРАБОТКА СТОЛБЦА AJ (Индекс 35) ---
        # if len(row_data) > 35 and isinstance(row_data[35], str) and "NA_VLOZENII_RUBL" in row_data[35]:
        #     # Формируем формулу с подстановкой номера текущей строки
        #     row_data[35] = нету

        # --- ОБРАБОТКА СТОЛБЦА AK (Индекс 36) ---
        if len(row_data) > 36 and isinstance(row_data[36], str) and "KOMMISSIA_POKUPKA" in row_data[36]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[36] = f"=F{current_row}*E{current_row}*0.0005"

        # --- ОБРАБОТКА СТОЛБЦА AL (Индекс 37) ---
        if len(row_data) > 37 and isinstance(row_data[37], str) and "KOMMISSIA_PRODAZA" in row_data[37]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[
                37] = f"=(T{current_row}*U{current_row}+V{current_row}*W{current_row}+X{current_row}*Y{current_row})*0.0005"

        # --- ОБРАБОТКА СТОЛБЦА AM (Индекс 38) ---
        if len(row_data) > 38 and isinstance(row_data[38], str) and "SCHET_UBITKI" in row_data[38]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[
                38] = f'=ЕСЛИ(AI{current_row}="убыток",'f' ЕСЛИ(AM{current_row - 1}="", 1, AM{current_row - 1}+1),'f' 0)'
        # ==================КОНЕЦ МОЛНИЯ=====================
        # ==================НАЧАЛО ОСНОВНОЙ=================
        # --- ОБРАБОТКА СТОЛБЦА S (Индекс 18) ---
        if len(row_data) > 18 and isinstance(row_data[18], str) and "O_BEZUBITOK_NACHALO" in row_data[18]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[18] = f"=F{current_row}*1.00093"
        # --- ОБРАБОТКА СТОЛБЦА T (Индекс 19) ---
        if len(row_data) > 19 and isinstance(row_data[19], str) and "O_ITOGO_1" in row_data[19]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[19] = (
                f'=ЕСЛИ(M{current_row}="",0,'f'(M{current_row}*N{current_row}-M{current_row}*N{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<M{current_row},(M{current_row}*N{current_row}-F{current_row}*N{current_row})*0.13,0)'
                f'-(F{current_row}*N{current_row}+F{current_row}*N{current_row}*0.0005)))')
        # --- ОБРАБОТКА СТОЛБЦА U (Индекс 20) ---
        if len(row_data) > 20 and isinstance(row_data[20], str) and "O_ITOGO_2" in row_data[20]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[20] = (
                f'=ЕСЛИ(O{current_row}="",0,'f'(O{current_row}*P{current_row}-O{current_row}*P{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<O{current_row},(O{current_row}*P{current_row}-F{current_row}*P{current_row})*0.13,0)'
                f'-(F{current_row}*P{current_row}+F{current_row}*P{current_row}*0.0005)))')
        # --- ОБРАБОТКА СТОЛБЦА V (Индекс 21) ---
        if len(row_data) > 21 and isinstance(row_data[21], str) and "O_ITOGO_3" in row_data[21]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[21] = (
                f'=ЕСЛИ(Q{current_row}="",0,'f'(Q{current_row}*R{current_row}-Q{current_row}*R{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<Q{current_row},(Q{current_row}*R{current_row}-F{current_row}*R{current_row})*0.13,0)'
                f'-(F{current_row}*R{current_row}+F{current_row}*R{current_row}*0.0005)))')
        # --- ОБРАБОТКА СТОЛБЦА W (Индекс 22) ---
        if len(row_data) > 22 and isinstance(row_data[22], str) and "O_ITOGO_ZARABOTOK" in row_data[22]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[22] = (
                f'=ЕСЛИ(E{current_row}<N{current_row}+P{current_row}+R{current_row},"ошибка кол-ва",'f'(ЕСЛИ(M{current_row}="",0,'
                f'(M{current_row}*N{current_row}-M{current_row}*N{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<M{current_row},(M{current_row}*N{current_row}-F{current_row}*N{current_row})*0.13,0)'
                f'-(F{current_row}*N{current_row}+F{current_row}*N{current_row}*0.0005)))'
                f'+ЕСЛИ(O{current_row}="",0,'
                f'(O{current_row}*P{current_row}-O{current_row}*P{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<O{current_row},(O{current_row}*P{current_row}-F{current_row}*P{current_row})*0.13,0)'
                f'-(F{current_row}*P{current_row}+F{current_row}*P{current_row}*0.0005)))'
                f'+ЕСЛИ(Q{current_row}="",0,'
                f'(Q{current_row}*R{current_row}-Q{current_row}*R{current_row}*0.0005-'
                f'ЕСЛИ(F{current_row}<Q{current_row},(Q{current_row}*R{current_row}-F{current_row}*R{current_row})*0.13,0)'
                f'-(F{current_row}*R{current_row}+F{current_row}*R{current_row}*0.0005))))'
                f'+J{current_row}*0.87+K{current_row}*0.87+L{current_row}*0.87)')
        # --- ОБРАБОТКА СТОЛБЦА X (Индекс 23) ---
        if len(row_data) > 23 and isinstance(row_data[23], str) and "O_PREDBEZUBITOK" in row_data[23]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[23] = (
                f'=ЕСЛИОШИБКА(ЕСЛИ(W{current_row}="ошибка кол-ва","ошибка кол-ва",'f'(F{current_row}*(N{current_row}+P{current_row}+R{current_row})-W{current_row})*1.00093/(N{current_row}+P{current_row}+R{current_row})))')
        # --- ОБРАБОТКА СТОЛБЦА Y (Индекс 24) ---
        if len(row_data) > 24 and isinstance(row_data[24], str) and "O_DNEI" in row_data[24]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[24] = f"=AA{current_row}-D{current_row}"
        # --- ОБРАБОТКА СТОЛБЦА Z (Индекс 25) ---
        if len(row_data) > 25 and isinstance(row_data[25], str) and "O_PROZENT" in row_data[25]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[25] = f"=ЕСЛИОШИБКА((W{current_row}/(E{current_row}*F{current_row}))*100)"
        # --- ОБРАБОТКА СТОЛБЦА AA (Индекс 26)     ДАТА ЗАКРЫТИЯ---
        # --- ОБРАБОТКА СТОЛБЦА AB (Индекс 27) ---
        if len(row_data) > 27 and isinstance(row_data[27], str) and "O_REZULTAT" in row_data[27]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[27] = (
                f'=ЕСЛИ(W{current_row}="ошибка кол-ва","ошибка кол-ва",'f'ЕСЛИ(E{current_row}>N{current_row}+P{current_row}+R{current_row},"процес",'
                f'ЕСЛИ(W{current_row}>0,"заработок","убыток")))')
        # --- ОБРАБОТКА СТОЛБЦА AC (Индекс 28) ---
        if len(row_data) > 28 and isinstance(row_data[28], str) and "O_VLOZENII_RUBL" in row_data[28]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[28] = f"=W{current_row}/Y{current_row}"
        # --- ОБРАБОТКА СТОЛБЦА AD (Индекс 29) ---
        if len(row_data) > 29 and isinstance(row_data[29], str) and "O_KOMISSIA_POKUPKA" in row_data[29]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[29] = f"=F{current_row}*E{current_row}*0.0005"
        # --- ОБРАБОТКА СТОЛБЦА AE (Индекс 30) ---
        if len(row_data) > 30 and isinstance(row_data[30], str) and "O_KOMISSIA_PRODAZA" in row_data[30]:
            # Формируем формулу с подстановкой номера текущей строки
            row_data[30] = f"=Q{current_row}*E{current_row}*0.0005"
        # ==================КОНЕЦ ОСНОВНОЙ==================
    # 4. Отправляем обновленные данные в таблицу
    response = gs.appendRangeValues_vstavka_strok(range=diapozon_dannich, values=znachenie)
    return response  # Можно вернуть для логирования


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
