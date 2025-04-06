"""This module is a assembler used to transform asm lang to machine lang"""

def binary_num_calc(num: str) -> str:
    """
    Takes as input integer number and converts it to binary

    Args:
        num (str): Decimal integer in str format.

    Returns:
        bit_num (str): Str representation of a bit number.
    """
    try:
        num = int(num)
    except ValueError as e:
        raise ValueError("Inputed value is not a integer") from e

    if num < 0 or num > 32767:
        raise Exception(f"Number needs to be in range 0 to 32768. Number of value {num} was inputed")
    bit_num = ""
    num_of_bits = 14
    while num_of_bits > -1:
        curr_bit_num = 2 ** num_of_bits
        if num - curr_bit_num > -1:
            num = num - curr_bit_num
            bit_num+= "1"
        else:
            bit_num += "0"
        num_of_bits -= 1

    bit_num = "0" + bit_num
    return bit_num

def symbol_cleaner(symbol: str) -> str:
    """
    This function is used to clean symbols.

    Args:
        symbol (str): Symbol form asm lang.

    Returns:
        str: Cleaned number
    """
    return symbol.replace("@", "")

def asm_to_mach_convertor(file : str) -> list:
    """
    Converts asm to machine code file.

    Args:
        file (str): File path

    Returns:
        file_struc (list): Structure of the text file.
    """
    file_struc = []
    with open(file, encoding="utf-8") as asm_file:
        for line in asm_file:

            line_read = line.rstrip().strip()

            if line_read.startswith("("):
                print(f"line {line_read} starts with: (")
            elif line_read.startswith("@"):
                print(f"line {line_read} starts with @")
                cleaned_dec = symbol_cleaner(line_read)
                bit_num = binary_num_calc(cleaned_dec)
                file_struc.append(bit_num)
            elif line_read.startswith("//") or len(line_read) < 1:
                print(f"line {line_read} is a comment or a whistespace. Ignore.")
            else:
                print(f"line {line_read} is a dest = comp; jmp")

    return file_struc

def main(file):
    """
    This func is used to translate asm lang to machine lang.

    Args:
        file (.asm file): File containing asm language.
    """
    file_struc = asm_to_mach_convertor(file)
    with open("Add.txt", "w", encoding="utf-8") as txt_file:
        for line in file_struc:
            txt_file.write(line + "\n")

if __name__ == '__main__':
    main("asm_progs/Add.asm")
