from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, ValidationError, computed_field
from typing import Any


# from typing import Optional


class Lightning(BaseModel):
    tiker: str
    action: str
    quantity: int | None = None
    price: float | None = None
    conclusion: str

    @field_validator('tiker', mode='before')
    def tiker_light(cls, tik):
        if not tik or not tik.strip():
            raise ValueError("Тикер не может быть пустым")
        return tik.strip().upper()

    @field_validator('action', mode='before')
    @classmethod
    def normalize_action(cls, v: Any) -> str:
        """Нормализует действие: приводит к единому формату
        Поддерживаемые варианты:
        • Покупка: 'b', 'buy', 'покупка', 'купить' → 'покупка'
        • Продажа: 's', 'sell', 'продажа', 'продать' → 'продажа'
        Применяется: strip(), lower(), маппинг синонимов"""
        # Защита от None и нестроковых значений
        if v is None:
            v = 'покупка'
        # Приведение к строке и нормализация
        normalized = str(v).strip().lower()
        # Маппинг синонимов покупки
        buy_aliases = {'', 'b', 'buy', 'покупка', 'купить', 'куплю'}
        # Маппинг синонимов продажи
        sell_aliases = {'s', 'sell', 'продажа', 'продать', 'продам'}
        if normalized in buy_aliases:
            return 'покупка'
        elif normalized in sell_aliases:
            return 'продажа'
        else:
            raise ValueError(f"Некорректное значение'{v}'.Варианты: {', '.join(sorted(buy_aliases | sell_aliases))}")

    @field_validator('quantity', mode='before')
    def quantity_light(cls, v):
        if v is None or v == "":
            return None
        if isinstance(v, str):
            v = v.strip().replace(' ', '')
            if not v.isdigit() and not (v.startswith('-') and v[1:].isdigit()):
                raise ValueError("Количество должно быть целым числом")
        return int(v)

    @field_validator('price', mode='before')
    def price_light(cls, v):
        if v is None or v == "":
            return None
        if isinstance(v, str):
            v = v.strip().replace(' ', '').replace(',', '.')  # ← Ключевое исправление для запятой!
            try:
                return float(v)
            except ValueError:
                raise ValueError("Цена должна быть числом (разделитель — точка или запятая)")
        return float(v)

    @field_validator('conclusion', mode='before')
    @classmethod
    def normalize_conclusion(cls, v: Any) -> str:
        """Нормализует вывод/заключение"""
        # Приведение к нижнему регистру. Приведение к строке и удаление пробелов по краям
        text = str(v).strip().lower()
        # Первая буква в верхний регистр, остальные остаются как есть (уже в lower)
        text = text[0].upper() + text[1:] if len(text) > 1 else text.upper()
        # Добавление точки в конце (без дублирования)
        if not text.endswith('.'):
            text += '.'
        return text


class StartIndication(BaseModel):
    text: str

    @field_validator('text', mode='before')
    def start_indication(cls, v: Any) -> str:
        """Нормализует вывод/заключение: удаляет переносы строк, схлопывает множественные пробелы"""
        text = ' '.join(str(v).split()).lower()
        # Первая буква в верхний регистр
        if text:
            text = text[0].upper() + text[1:]
        else:
            text = ''  # пустая строка остаётся пустой
            # Добавление точки в конце (без дублирования)
        if not text.endswith('.'):
            text += '.'
        return text
