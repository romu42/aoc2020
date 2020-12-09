#!/usr/bin/env python3

import logging
import sys
from itertools import combinations
from collections import deque


# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file) as f:
        return [int(x) for x in f.read().split('\n')]

def find_pairs(lst: list, preamble: int) -> list:
    logging.info(f'preamble = {preamble}')
    logging.info(f'input list = {lst}')
    logging.info(f'starter slice = {lst[preamble:]}')
    d = deque(lst[0:preamble], maxlen=preamble)
    for element in lst[preamble:]:
        logging.info(d)
        logging.info(f'{[pair for pair in combinations(d, 2) if sum(pair) == element]} - {element}')
        short_lst = [pair for pair in combinations(d, 2) if sum(pair) == element]
        if len(short_lst) == 0:
            print(element)
            exit()
        d.append(element)


def find_cont(lst: list, goal):
    slice_start = 0
    slice_stop = slice_start + 1
    while True:
        work_slice = lst[slice_start:slice_stop]
    # for counter in range(0, len(lst)):
        if sum(work_slice) == goal:
            logging.info(f'{work_slice}')
            logging.info(f'{min(work_slice) + max(work_slice)}')
            exit()
        elif sum(work_slice) > goal:
            slice_start = slice_start + 1
            slice_stop = slice_start + 1
        else:
            slice_stop = slice_stop + 1




if __name__ == '__main__':
    # working_input = (clean_input("puzzle_input_test"))
    working_input = clean_input('puzzle_input')
    # find_pairs(working_input, 25)
    # find_cont(working_input, 127)
    find_cont(working_input, 1504371145)
