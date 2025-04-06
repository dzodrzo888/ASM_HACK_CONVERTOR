"""This module is a assembler used to transform asm lang to machine lang"""
import os
import helpers
import bin_convertor
import sym_tab_man

class ASMConvertor:
    """
    This class is used to convert ASM to machine language.
    """
    def __init__(self):
        self.c_cmd_conv_cls = bin_convertor.CCommandConvertor()
        self.symbol_table_cls = sym_tab_man.SymbolTable()
        self.file_struc = []

    def add_symbols_to_table(self, file : str):
        """
        Adds symbols to table.

        Args:
            file (str): file_path
        """
        if not isinstance(file, str):
            raise TypeError("File path is not a string!")
        try:
            with open(file, encoding="utf-8") as asm_file:

                i = 0
                for line in asm_file:

                    line_read = line.rstrip().strip()

                    if line_read.startswith("("):
                        print(f"line {line_read} starts with: (")
                        label = line_read[1:-1].strip()
                        self.symbol_table_cls.symbol_adder(label, i)
                    elif line_read.startswith("//") or len(line_read) < 1:
                        print(f"line {line_read} is a comment or a whistespace. Ignore.")
                        continue
                    else:
                        i += 1
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File path: {file} doesnt exist!") from e

    def convert_asm_to_machine(self, file: str):
        """
        Converts asm to machine language. Also adds 

        Args:
            file (str): file path
        """
        if not isinstance(file, str):
            raise TypeError("File path is not a string!")
        try:
            with open(file, encoding="utf-8") as asm_file:
                for line in asm_file:

                    line_read = line.rstrip().strip()

                    if line_read.startswith("@"):
                        print(f"line {line_read} starts with @")
                        cleaned_dec = helpers.symbol_cleaner(line_read)

                        if not isinstance(cleaned_dec, int) and cleaned_dec not in self.symbol_table_cls.table:
                            self.symbol_table_cls.variable_adder(cleaned_dec)
                            cleaned_dec = self.symbol_table_cls.curr_ram_var

                        if not isinstance(cleaned_dec, int) and cleaned_dec in self.symbol_table_cls.table:
                            cleaned_dec = self.symbol_table_cls.get_address(cleaned_dec)

                        bit_num = bin_convertor.binary_num_calc(cleaned_dec)
                        self.file_struc.append(bit_num)
                    elif line_read.startswith("//") or len(line_read) < 1 or line_read.startswith("("):
                        print(f"line {line_read} is a comment or a whistespace. Ignore.")
                        continue
                    else:
                        print(f"line {line_read} is a dest = comp; jmp")
                        c_cmd_bin = self.c_cmd_conv_cls.dest_comp_jump_bin_convertor(line_read)
                        self.file_struc.append(c_cmd_bin)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File path: {file} doesnt exist!") from e

    def file_struc_polluter(self, file: str) -> list:
        """
        Returns file struc.

        Returns:
            file_struc (list): Structure of the text file.
        """
        if not isinstance(file, str):
            raise TypeError("File path is not a string!")
        try:
            self.add_symbols_to_table(file)
            self.convert_asm_to_machine(file)
            return self.file_struc
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File path: {file} doesnt exist!") from e

    def machine_lang_file_writter(self, file: str):
        """
        This func is used to translate asm lang to machine lang.

        Args:
            file (.asm file): File containing asm language.
        """
        if not isinstance(file, str):
            raise TypeError("File path is not a string!")

        try:
            filename, _ = os.path.splitext(file)
            file_struc = self.file_struc_polluter(file)
            with open(f"{filename}.hack", "w", encoding="utf-8") as txt_file:
                for line in file_struc:
                    txt_file.write(line + "\n")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File path: {file} doesnt exist!") from e

if __name__ == '__main__':
    file_path = input("Specify the file path: ")
    asm_conv_class = ASMConvertor()
    asm_conv_class.machine_lang_file_writter(file_path)
