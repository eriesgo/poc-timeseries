# infrastructure.py

from typing import List, Optional, Tuple, cast
import os
import psycopg2
from psycopg2 import sql
import logging

def connect_to_database() -> psycopg2.extensions.connection:
    host: str = os.environ.get("POSTGRES_HOST", "localhost")
    port: str = os.environ.get("POSTGRES_PORT", "5432")
    user: str = os.environ.get("POSTGRES_USER", "postgres")
    password: str = os.environ.get("TIMESCALEDB_PASSWORD", "")
    database: str = os.environ.get("POSTGRES_DB", "timeseries")

    connection: psycopg2.extensions.connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

def get_symbols_repository() -> List[Tuple[str, str]]:
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            select_symbols_query: sql.SQL = sql.SQL("""
                SELECT symbol, name FROM company
            """)
            cursor.execute(select_symbols_query)
            symbols: List[Tuple[str, str]] = [(row[0], row[1]) for row in cursor.fetchall()]

        connection.close()
        return symbols

    except Exception as e:
        logging.error(f"An error occurred while retrieving symbols: {str(e)}")
        raise


def get_symbol_details_repository(symbol: str) -> Tuple[str, str] | None:
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            select_symbol_query: sql.SQL = sql.SQL("""
                SELECT symbol, name FROM company WHERE symbol = %s
            """)
            cursor.execute(select_symbol_query, (symbol,))
            symbol_details: Optional[Tuple[str, str]] = cast(Optional[Tuple[str, str]], cursor.fetchone())

        connection.close()
        return symbol_details

    except Exception as e:
        logging.error(f"An error occurred while retrieving symbols: {str(e)}")
        raise
