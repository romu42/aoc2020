#!/usr/bin/env python3

import logging
import sys
from itertools import combinations
from itertools import permutations
from collections import defaultdict


# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, 'r') as f:
        return [int(x) for x in f.read().split('\n')]


def get_deltas_sum(lst: list):
    working_lst = sorted(lst)
    logging.info(working_lst)
    working_lst = [0] + working_lst + [max(working_lst) + 3]
    logging.info(working_lst)
    delta_dict = {1:0, 2:0, 3:0}
    unremovable = set()
    for counter in range(0, len(working_lst)-1):
        delta = working_lst[counter+1] - working_lst[counter]
        if delta == 1:
            delta_dict[1] = delta_dict[1] + 1
        elif delta == 2:
            delta_dict[2] = delta_dict[2] + 1
        elif delta == 3:
            delta_dict[3] = delta_dict[3] + 1
        else:
            logging.debug(f'Something went wrong bob')
        logging.debug(delta)
    logging.info(f'the answer for day10 pt1 is: {delta_dict[1] * delta_dict[3]}')
    logging.debug(delta_dict)
    # for counter, item in enumerate(unremovable):
    #     logging.info(f'{counter} - {item} - {working_lst[item]}')

    counter = 0
    tbr = []
    #while counter <= len(working_lst):
    working_lst = working_lst + [0, 0, 0]
    while working_lst[counter] != working_lst[-5]:
        bob = len(working_lst)
        place0 = working_lst[counter]
        place1 = working_lst[counter + 1]
        place2 = working_lst[counter + 2]
        place3 = working_lst[counter + 3]

        if working_lst[counter+1] - working_lst[counter] == 1 and working_lst[counter + 2] - working_lst[counter] == 3:
            counter = counter + 1
        elif working_lst[counter+1] - working_lst[counter] == 1 and working_lst[counter + 2] - working_lst[counter] == 4:
            counter = counter + 2
        elif working_lst[counter+1] - working_lst[counter] == 1 and working_lst[counter + 2] - working_lst[counter] == 2:
            if working_lst[counter + 3] - working_lst[counter] == 3:
                tbr = tbr + working_lst[counter+1:counter+3]
                counter = counter + 3
            else:
                tbr = tbr + working_lst[counter+1:counter+2]
                counter = counter + 2
        elif working_lst[counter+1] - working_lst[counter] == 3:
                counter = counter + 1
        elif working_lst[counter] == working_lst[-4]:
            break
    logging.info(working_lst)
    logging.info(tbr)
    # perm = [x for x in permutations(tbr, len(tbr))]
    counter = len(tbr)
    comb = []
    while counter:
        comb = comb + [x for x in combinations(tbr, counter)]
        counter = counter - 1
    # print(f'perm = {perm}')
    print(f'comb = {comb}')
    print(len(comb) + 1)



def get_delta_3(lst: list):
    pass

if __name__ == '__main__':
    working_input = (clean_input("puzzle_input_test"))
    # working_input = clean_input('puzzle_input')
    # working_input = clean_input('puzzle_input_test_short')
    logging.info(working_input)
    get_deltas_sum(working_input)
    # get_delta_3(working_input)
