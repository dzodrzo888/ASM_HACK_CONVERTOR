"""This file contains functions to convert nums to bin and comp,dest,jump command to bin."""
import config
class CCommandConvertor:
    """
    Class used to convert computation command to binary.
    """
    def __init__(self):
        self.config = config

    def dest_comp_jump_parser(self, command: str) -> list:
        """
        Funciton used to parse ASM command to dest, comp, jump.

        Args:
            command (str): ASM command.

        Returns:
            list: List containing parsed ASM command (dest, comp, jump).
        """
        comp_jump = None
        dest = comp = jump =  "null"

        if "=" in command and ";" in command:
            dest, comp_jump = command.split("=")
            comp, jump = comp_jump.split(";")
        elif "=" in command and ";" not in command:
            dest, comp = command.split("=")
        elif "=" not in command and ";" in command:
            comp, jump = command.split(";")

        return [dest, comp, jump]

    def comp_bin_convertor(self, comp_command: str) -> str:
        """
        Converts comp command to binary

        Args:
            comp_command (str): Comp command.

        Returns:
            str: Comp command in binary
        """
        a = "0"

        if "M" in comp_command:
            
            comp_command = comp_command.replace("M", "A")
            a = "1"
        
        comp_partial = self.config.comp.get(comp_command)
        return a + comp_partial

    def dest_comp_jump_bin_convertor(self, command: str) -> str:
        """_summary_

        Args:
            command (str): ASM command.

        Returns:
            str: ASM command in binary.
        """
        bin_str = ""

        commands = self.dest_comp_jump_parser(command)

        dest_bin = self.config.dest.get(commands[0])
        comp_bin = self.comp_bin_convertor(commands[1])
        jump_bin = self.config.jump.get(commands[2])

        bin_str = "111" + comp_bin + dest_bin + jump_bin
        print(bin_str)
        return bin_str

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