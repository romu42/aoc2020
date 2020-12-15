#!/usr/bin/env python3

import logging
import sys
from itertools import product
import re

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input_pt1(file) -> list:
    with open(file, 'r') as f:
        instructions = [x for x in f.read().split('\n')]
    mask = []
    memory = {}
    for item in instructions:
        if 'mask' in item:
            logging.debug(f'{item}')
            mask = [x for x in item.split(' = ')[1]]
            logging.debug(f'{item}')
        else:
            logging.debug(f'{item}')
            mem = re.findall(r'\d+', item)
            place = mem[0]
            bits = [x for x in f'{int(mem[1]):036b}']
            logging.debug(f'{place} points to {bits}')
            memory[place] = bits
            for counter, bit in enumerate(mask):
                if bit == 'X':
                    next
                else:
                    memory[place][counter] = bit
    logging.debug(memory)
    total = 0
    for k,v in memory.items():
        total = total + int("".join([x for x in v]),2)
    logging.info(f'the answer for pt1 is: {total}')
    return(f'bob is done here!')


def clean_input_pt2(file) -> list:
    with open(file, 'r') as f:
        instructions = [x for x in f.read().split('\n')]
    mask = []
    memory2 = {}
    for item in instructions:
        if 'mask' in item:
            logging.debug(f'{item}')
            mask = [x for x in item.split(' = ')[1]]
            logging.debug(f'{item}')
        else:
            logging.info(f'{item}')
            mem = re.findall(r'\d+', item)
            input_value = int(mem[1])
            logging.info(mem[0])
            place = [x for x in f'{int(mem[0]):036b}']
            logging.info(f'place {place} points to {input_value}')
            logging.info(f'mask  {mask}')
            for counter, bit in enumerate(mask):
                if bit == 'X' or bit == '0':
                    next
                else:
                    place[counter] = bit
            mem = place
            logging.info(f'mem   {mem}')
            logging.debug((f'memory place = {mem}'))
            logging.debug(mask)
            r = mask.count('X')
            logging.debug(r)
            indexes = [index for index, x in enumerate(mask) if x == 'X']
            for index in indexes:
                logging.debug(mask[index])
            logging.debug(indexes)
            # replacements = ['a', 'b']
            replacements = ['0', '1']
            replacements = [replacement for replacement in product(replacements, repeat=r)]
            logging.info(replacements)
            for group in replacements:
                for index, value in zip(indexes, group):
                    mem[index] = value
                logging.debug(f'{mem}')
                memory = "".join(mem)
                logging.info(memory)
                put_it_here = (int("".join([x for x in memory]), 2))
                logging.info((f'{put_it_here} - {input_value}'))
                memory2[put_it_here] = input_value
    logging.debug(memory)
    total = 0
    for k,v in memory2.items():
        total = total + v
    logging.info(f'the answer for pt1 is: {total}')
    return(f'bob is done here!')




if __name__ == '__main__':
    # working_lst = clean_input_pt1('puzzle_input_test')
    # working_lst = clean_input_pt1('puzzle_input')
    # working_lst = clean_input_pt2('puzzle_input_test')
    working_lst = clean_input_pt2('puzzle_input')
    logging.info(working_lst)
