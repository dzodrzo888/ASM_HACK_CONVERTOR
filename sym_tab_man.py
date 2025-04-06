"""Module to keep a symbols table and add symbols and variables to it."""
import config

class SymbolTable:
    """
    Adds symbols and variables to the symbol table.
    """
    def __init__(self):
        self.table =  config.symbol_table
        self.curr_ram_var = 16

    def symbol_adder(self, symbol:str, address: str):
        """
        Adds symbol to the symbol table

        Args:
            symbol (str): Symbol to be read in the table.
            address (str): Address of the symbol.
        """
        if symbol not in self.table:
            self.table[symbol] = address

    def variable_adder(self, variable: str):
        """
        Adds variable to a table.

        Args:
            variable (str): Var to be read into the table
        """
        if variable not in self.table:
            self.table[variable] = self.curr_ram_var
            self.curr_ram_var += 1

    def get_address(self, symbol: str) -> int:
        """
        Gets the address of a symbol.

        Args:
            symbol (str): Symbol to be read in the table

        Returns:
            int: Returns the address of the symbol.
        """
        return self.table[symbol]
