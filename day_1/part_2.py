#!/usr/bin/python3
"""Day 1: Trebuchet?! - Part Two"""
import sys
from os import chdir
from os.path import dirname
from re import findall
from sys import executable
from sys import path as syspath

DIGITS: dict[str, str] = {
    **{str(i): str(i) for i in range(1, 10)},
    'one':     '1',
    'two':     '2',
    'three':   '3',
    'four':    '4',
    'five':    '5',
    'six':     '6',
    'seven':   '7',
    'eight':   '8',
    'nine':    '9'
}


def use_main_dir() -> None:
    """Use the directory of the main script as working directory."""
    chdir(dirname(executable) if getattr(sys, 'frozen', False) else syspath[0])


def find_digit(string: str, *, reverse: bool = False) -> str:
    """Find first digit in string."""
    pattern: str = f'(?=({"|".join(DIGITS.keys())}))'
    matches: list[str] = findall(pattern, string)
    if not matches:
        raise ValueError("String doesn't contain digits.")

    return DIGITS[matches[-1 if reverse else 0]]


def main() -> None:
    """Calculate sum."""
    with open('input.txt', encoding='utf8') as file:
        total: int = 0
        for line in file:
            first_digit:       str = find_digit(line)
            last_digit:        str = find_digit(line, reverse=True)
            two_digit_number:  str = first_digit + last_digit
            calibration_value: int = int(two_digit_number)
            total += calibration_value

        print(f'Total={total}')


if __name__ == '__main__':
    use_main_dir()
    main()
