#!/usr/bin/env python3

import logging
import sys
from collections import deque, defaultdict
from functools import partial

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, 'r') as f:
        return [x for x in f.read().split(',')]



def get_2020(lst: list):
    count = 0
    memory = defaultdict(partial(deque, maxlen=2))
    for number in lst:
        count = count + 1
        memory[int(number)] = deque([count], 2)
        logging.debug(f'{count} - {number}')
        last_number = number

    logging.debug(memory)
    # while count <= 2019:
    while count <= (30000000 - 1):
        if last_number in memory.keys() and len(memory[last_number]) > 1:
            count = count + 1
            diff = memory[last_number][0] - memory[last_number][1]
            memory[diff].appendleft(count)
            logging.debug(f'{count} - {diff}')
            last_number = diff
        else:
            count = count + 1
            memory[0].appendleft(count)
            logging.debug(f'{count} - {0}')
            last_number = 0



    logging.debug(f'{count} - {last_number}')
    return f'{count} - {last_number}'


if __name__ == '__main__':
    # working_lst = clean_input('puzzle_input_test')
    working_lst = clean_input('puzzle_input')
    logging.debug(working_lst)
    logging.info(get_2020(working_lst))
