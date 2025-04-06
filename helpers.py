"""This module contains helper functions."""
def symbol_cleaner(symbol: str) -> str:
    """
    This function is used to clean symbols.

    Args:
        symbol (str): Symbol form asm lang.

    Returns:
        str: Cleaned number
    """
    if not isinstance(symbol, str):
            raise TypeError("Command is not a string!")

    return symbol.replace("@", "")