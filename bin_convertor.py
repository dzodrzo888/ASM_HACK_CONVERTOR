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
        if not isinstance(command, str):
            raise TypeError("Command is not a string!")

        comp_jump = None
        dest = comp = jump =  "null"

        if "=" in command and ";" in command:
            dest, comp_jump = command.split("=")
            comp, jump = comp_jump.split(";")
        elif "=" in command and ";" not in command:
            dest, comp = command.split("=")
        elif "=" not in command and ";" in command:
            comp, jump = command.split(";")
        else:
            raise TypeError(f"Command={command} is not a ASM command!")

        return [dest, comp, jump]

    def comp_bin_convertor(self, comp_command: str) -> str:
        """
        Converts comp command to binary

        Args:
            comp_command (str): Comp command.

        Returns:
            str: Comp command in binary
        """
        if not isinstance(comp_command, str):
            raise TypeError("comp_command is not a string!")
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
        if not isinstance(command, str):
            raise TypeError("Command is not a string!")

        bin_str = ""

        commands = self.dest_comp_jump_parser(command)

        dest_bin = self.config.dest.get(commands[0])
        comp_bin = self.comp_bin_convertor(commands[1])
        jump_bin = self.config.jump.get(commands[2])

        if None in (dest_bin, comp_bin, jump_bin):
            raise ValueError(f"Invalid C-command parts: dest={commands[0]}, comp={commands[1]}, jump={commands[2]}")

        bin_str = "111" + comp_bin + dest_bin + jump_bin

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
    except TypeError as e:
        raise TypeError("Inputed value is not a integer") from e

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
