"""This module is a assembler used to transform asm lang to machine lang"""
import helpers
import bin_convertor


def asm_to_mach_convertor(file : str) -> list:
    """
    Converts asm to machine code file.

    Args:
        file (str): File path

    Returns:
        file_struc (list): Structure of the text file.
    """
    file_struc = []
    c_cmd_conv_cls = bin_convertor.CCommandConvertor()
    with open(file, encoding="utf-8") as asm_file:
        for line in asm_file:

            line_read = line.rstrip().strip()

            if line_read.startswith("("):
                print(f"line {line_read} starts with: (")
            elif line_read.startswith("@"):
                print(f"line {line_read} starts with @")
                cleaned_dec = helpers.symbol_cleaner(line_read)
                bit_num = bin_convertor.binary_num_calc(cleaned_dec)
                file_struc.append(bit_num)
            elif line_read.startswith("//") or len(line_read) < 1:
                print(f"line {line_read} is a comment or a whistespace. Ignore.")
            else:
                print(f"line {line_read} is a dest = comp; jmp")
                c_cmd_bin = c_cmd_conv_cls.dest_comp_jump_bin_convertor(line_read)
                file_struc.append(c_cmd_bin)

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
