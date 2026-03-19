import os
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine, func, select
from sqlalchemy.orm import sessionmaker


# Загружаем переменные из .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env.wallet")
db_path_str = os.getenv("DB_PATH")
path_database = Path(__file__).resolve().parent.parent.parent
# Получаем относительный путь из .env
# через оператор /
db_path = path_database / db_path_str
db_path = db_path.resolve()  # Превращаем в абсолютный для надежности
DATABASE_URL = f"sqlite:///{db_path}"
engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData()
# создадим нужные таблицы
buyinform_table = Table("buyinform", metadata, autoload_with=engine)
mytrade_results_table = Table("mytrade_results", metadata, autoload_with=engine)
what_in_briefcase_table = Table("buyinform", metadata, autoload_with=engine)
# Создаем сессию и делаем запрос
SessionLocal = sessionmaker(bind=engine)


def total_trade_by_day(days=8):
    """ВЫРУЧКА ЗА ДЕНЬ (8 ДНЕЙ)"""
    today = datetime.now()
    week_ago = today - timedelta(days=days)
    with SessionLocal() as session:
        # Строим запрос
        stmt = (
            select(
                func.date(mytrade_results_table.c.date_sale).label("sale_date"),  # DATE(date_sale)
                func.sum(mytrade_results_table.c.net_profit).label("total_net"),  # SUM(net_profit)
                func.sum(mytrade_results_table.c.percent_profit).label("total_percent"),  # SUM(percent_profit)
            )
            .where(mytrade_results_table.c.date_sale >= week_ago)
            .group_by(
                func.date(mytrade_results_table.c.date_sale)  # GROUP BY DATE(date_sale)
            )
            .order_by(
                func.date(mytrade_results_table.c.date_sale)  # ORDER BY для удобства
            )
        )
        result_week = session.execute(stmt)
        rows = result_week.mappings().all()
        return rows


def total_trade_by_moth():
    """ВЫРУЧКА ЗА МЕСЯЦ"""
    with SessionLocal() as session:
        # Строим запрос
        stmt = select(
            func.strftime("%Y-%m", mytrade_results_table.c.date_sale).label("sale_month"),
            func.sum(mytrade_results_table.c.net_profit).label("total_net"),
            func.count(mytrade_results_table.c.id).label("deals_count"),
        ).group_by(func.strftime("%Y-%m", mytrade_results_table.c.date_sale))
        result_week = session.execute(stmt)
        rows = result_week.mappings().all()
        return rows


def what_in_briefcase():
    """ЧТО В ПОРТФЕЛЕ"""
    with SessionLocal() as session:
        # Строим запрос
        stmt = select(what_in_briefcase_table).where(what_in_briefcase_table.c.quantity_buy != 0)
        result_week = session.execute(stmt)
        rows = result_week.mappings().all()
        return rows


if __name__ == "__main__":
    print(what_in_briefcase())
