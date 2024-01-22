# hexagonal.py

from typing import List, Dict, Tuple, Optional, Callable

def get_symbols_use_case(get_symbols_repository: Callable[[], List[Tuple[str, str]]]) -> List[Dict[str, str]]:
    symbols = get_symbols_repository()
    return [{'symbol': row[0], 'name': row[1]} for row in symbols]

def get_symbol_details_use_case(symbol: str, get_symbol_details_repository: Callable[[str], Optional[Tuple[str, str]]]) -> Dict[str, str]:
    details = get_symbol_details_repository(symbol)
    return {'symbol': details[0], 'name': details[1]} if details else {}
