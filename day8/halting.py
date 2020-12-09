#!/usr/bin/env python3

import logging
import sys
import copy


logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)


def clean_input(file) -> list:
    with open(file) as f:
        temp_list = []
        for x in f.read().split("\n"):
            action, count = x.split(' ')
            temp_list.append([action, int(count), False])
        return temp_list


def find_loop(instructions: list) -> int:
    accumulator = 0
    place = 0
    for x in range(0, len(instructions) + 1):
        if instructions[place][2] is True:
            print(accumulator)
            exit()
        elif instructions[place][0] == 'nop' and instructions[place][2] is False:
            instructions[place][2] = True
            # print(f'place{place} {instructions[place]}')
            place = place + 1
        elif instructions[place][0] == 'acc' and instructions[place][2] is False:
            # print(f'place{place} {instructions[place]}')
            instructions[place][2] = True
            accumulator = accumulator + instructions[place][1]
            place = place + 1
        elif instructions[place][0] == 'jmp' and instructions[place][2] is False:
            # print(f'place{place} {instructions[place]}')
            instructions[place][2] = True
            place = place + instructions[place][1]

def test_loop(instructions: list, control: list) -> int:
    counter = 0
    for x in range(0, len(control)):
        counter = counter + 1
        test_list = copy.deepcopy(instructions)
        if instructions[x][0] == 'nop':
            test_list[x][0] = 'jmp'
            fix_loop(test_list, x)
        elif instructions[x][0] == 'jmp':
            test_list[x][0] = 'nop'
            fix_loop(test_list, x)
        else:
            next


def fix_loop(instructions: list, changed: int) -> int:
    accumulator = 0
    place = 0
    for x in range(0, len(instructions)):
        if place == len(instructions) :
            print(f'found answer with fixed loop: {accumulator}')
            exit()
        if instructions[place][2] is True:
            return
        elif instructions[place][0] == 'nop' and instructions[place][2] is False:
            instructions[place][2] = True
            place = place + 1
        elif instructions[place][0] == 'acc' and instructions[place][2] is False:
            instructions[place][2] = True
            accumulator = accumulator + instructions[place][1]
            place = place + 1
        elif instructions[place][0] == 'jmp' and instructions[place][2] is False:
            instructions[place][2] = True
            place = place + instructions[place][1]

if __name__ == '__main__':
    # working_input = (clean_input("puzzle_input_test"))
    working_input = clean_input('puzzle_input')
    control = copy.deepcopy(working_input)
    # find_loop(working_input)
    test_loop(working_input, control)
