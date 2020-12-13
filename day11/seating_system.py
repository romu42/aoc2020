#!/usr/bin/env python3

import logging
import sys
from itertools import combinations
from itertools import permutations
from collections import defaultdict
import copy


# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, 'r') as f:
        seating = [f'.{x}.' for x in f.read().split('\n')]
        extra_rows = '.' * len(seating[0])
        seating.insert(0, extra_rows)
        seating.append(extra_rows)
        return seating

def create_seating_dict(lst: list) -> dict:
    logging.debug(lst)
    seating = defaultdict(dict)
    row = 0
    for seats in lst:
        column = 0
        for seat in seats:
            seating[row][column] = seat
            column = column + 1
        row = row + 1
    return seating


def print_seating_chart(seating_dict: dict):
    row = 0
    for seats in seating_dict.keys():
        num_rows = len(seating_dict.keys())
        if row == 0:
            row = row + 1
            next
        elif row == num_rows - 1:
            break
        row_seating = []
        column = 0
        for seat in seating_dict[seats].keys():
            num_seats = len(seating_dict[seats].keys())
            if column == 0:
                column = column + 1
                next
            elif column == num_seats - 1:
                break
            row_seating.append(seating_dict[row][column])
            column = column + 1
        logging.debug(f'{"".join(row_seating)}')
        row = row + 1


def run_ruleset(seating_dict: dict) -> dict:
    occupied_seats = 0
    temp_seating_chart = copy.deepcopy(seating_dict)
    row = 0
    for seats in seating_dict.keys():
        num_rows = len(seating_dict.keys())
        if row == 0:
            row = row + 1
            next
        elif row == num_rows - 1:
            break
        row_seating = []
        column = 0
        for seat in seating_dict[seats].keys():
            num_seats = len(seating_dict[seats].keys())
            if column == 0:
                column = column + 1
                next
            elif column == num_seats - 1:
                break
            temp_seating_chart[row][column] = check_adjacent_seats(seating_dict, seating_dict[row][column], row, column)
            if temp_seating_chart[row][column] == '#':
                occupied_seats = occupied_seats + 1
            column = column + 1
        row = row + 1
    return temp_seating_chart, temp_seating_chart == seating_dict, occupied_seats


def check_adjacent_seats(seating_dict: dict, seat: str, row: int, column: int) -> str:
    adjacent_seats = []
    adjacent_seats.append(seating_dict[row - 1][column - 1])
    adjacent_seats.append(seating_dict[row - 1][column])
    adjacent_seats.append(seating_dict[row - 1][column + 1])
    adjacent_seats.append(seating_dict[row][column - 1])
    adjacent_seats.append(seating_dict[row][column + 1])
    adjacent_seats.append(seating_dict[row + 1][column - 1])
    adjacent_seats.append(seating_dict[row + 1][column])
    adjacent_seats.append(seating_dict[row + 1][column + 1])
    if seating_dict[row][column] == 'L' and '#' not in adjacent_seats:
        return '#'
    elif seating_dict[row][column] == '#' and adjacent_seats.count('#') > 3:
        return 'L'
    else:
        return seating_dict[row][column]


if __name__ == '__main__':
    # working_lst = clean_input('puzzle_input_test')
    working_lst = clean_input('puzzle_input')
    ferry_seating = (create_seating_dict(working_lst))
    # print_seating_chart(ferry_seating)
    logging.debug(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    ferry_seating, status, num_seats_occupied = run_ruleset(ferry_seating)
    logging.debug(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    logging.debug(f'number of seats occupied after last run: {num_seats_occupied}')
    # print_seating_chart(ferry_seating)
    while not status:
        ferry_seating, status, num_seats_occupied = run_ruleset(ferry_seating)
        logging.debug(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print_seating_chart(ferry_seating)
    logging.info(f'number of seats occupied after last run: {num_seats_occupied}')
