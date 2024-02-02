"""Module providing domain logic"""

from typing import Callable


def get_symbols_use_case(
    get_symbols_repository: Callable[[], list[tuple[str, str]]]
) -> list[dict[str, str]]:
    symbols = get_symbols_repository()
    return [{"symbol": row[0], "name": row[1]} for row in symbols]


def get_symbol_details_use_case(
    symbol: str,
    get_symbol_details_repository: Callable[[str], tuple[str, str]|None],
) -> dict[str, str]:
    details: tuple[str, str]|None = get_symbol_details_repository(symbol)
    return {"symbol": details[0], "name": details[1]} if details else {}
