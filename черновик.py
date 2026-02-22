from wallett.googleteable import *

# Маппинг месяца → буква столбца в Google Таблице (январь = B, февраль = C, ...)
MONTH_TO_COLUMN = {1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M"}


def average_monthly_expenses():
    """РАСЧИТЫВАЕТ СРЕДНИЕ РАСХОДЫ ЗА 12 МЕС"""
    try:
        dds_expenses = 0
        quantity = 0
        for month in range(1, 13, 1):
            column = MONTH_TO_COLUMN.get(month)
            mont = float(Read(Nazvanie_operazii="ЧИТАЕМ ДДС", range=f"ДДС,PNL!{column}18")[0])
            if mont == 0.0:
                quantity += 0
                dds_expenses += mont
            else:
                dds_expenses += mont
                quantity += 1
        average_month_expenses = round(dds_expenses / quantity, 2)
        return average_month_expenses
    except Exception as e:
        print(e)
        # logi.err.info(f"average_monthly_expenses() ошибка СРЕД РАСХ handlers/handler_message.py , Exception as e : {e}")


if __name__ == "__main__":
    i = average_monthly_expenses()
    print(i)
