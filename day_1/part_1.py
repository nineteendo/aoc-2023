#!/usr/bin/python3
"""Day 1: Trebuchet?! - Part One"""
import sys
from os import chdir
from os.path import dirname
from re import findall
from sys import executable
from sys import path as syspath


def use_main_dir() -> None:
    """Use the directory of the main script as working directory."""
    chdir(dirname(executable) if getattr(sys, 'frozen', False) else syspath[0])


def find_digit(string: str, *, reverse: bool = False) -> str:
    """Find first digit in string."""
    matches: list[str] = findall('\\d', string)
    if not matches:
        raise ValueError("String doesn't contain digits.")

    return matches[-1 if reverse else 0]


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
