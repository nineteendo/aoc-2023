#!/usr/bin/python3
"""Day 2: Cube Conundrum - Part One"""
import sys
from os import chdir
from os.path import dirname
from sys import executable
from sys import path as syspath

COLORS: dict[str, int] = {
    'red':   12,
    'green': 13,
    'blue':  14
}


def use_main_dir() -> None:
    """Use the directory of the main script as working directory."""
    chdir(dirname(executable) if getattr(sys, 'frozen', False) else syspath[0])


def partition_colon(i: int, string: str) -> tuple[str, str]:
    """Partition string at colon."""
    prefix: str
    colon:  str
    suffix: str
    prefix, colon, suffix = string.strip('\n').partition(':')
    if colon != ':':
        raise RuntimeError(f'Line {i}: missing colon')

    return prefix, suffix


def get_game_id(i: int, string: str) -> int:
    """Get game id from string."""
    game:      str
    space:     str
    id_string: str
    game, space, id_string = string.strip().partition(' ')
    id_string = id_string.strip()
    if game != 'Game' or space != ' ' or not id_string.isdigit():
        raise RuntimeError(f'Line {i}: prefix malformed')

    return int(id_string)


def get_subset(i: int, string: str) -> tuple[int, str]:
    """Get subset from string."""
    count_string: str
    color:        str
    count_string, space, color = string.strip().partition(' ')
    color = color.strip()
    if not count_string.isdigit() or space != ' ' or color not in COLORS:
        raise RuntimeError(f'Line {i}: subset malformed')

    count: int = int(count_string)
    return count, color


def evaluate_game(i: int, string: str) -> int:
    """Evaluate game."""
    prefix: str
    suffix: str
    prefix, suffix = partition_colon(i, string)
    game_id: int = get_game_id(i, prefix)
    for subsets_string in suffix.split(';'):
        for subset_string in subsets_string.split(','):
            count: int
            color: str
            count, color = get_subset(i, subset_string)
            if count > COLORS[color]:
                return 0

    return game_id


def main() -> None:
    """Calculate sum."""
    with open('input.txt', encoding='utf8') as file:
        total: int = 0
        for i, line in enumerate(file):
            total += evaluate_game(i, line)

        print(f'Total={total}')


if __name__ == '__main__':
    use_main_dir()
    main()
