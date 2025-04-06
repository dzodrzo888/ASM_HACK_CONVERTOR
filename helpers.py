"""This module contains helper functions."""
def symbol_cleaner(symbol: str) -> str:
    """
    This function is used to clean symbols.

    Args:
        symbol (str): Symbol form asm lang.

    Returns:
        str: Cleaned number
    """
    return symbol.replace("@", "")