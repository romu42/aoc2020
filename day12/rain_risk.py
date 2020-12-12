#!/usr/bin/env python3

import logging
import sys
from collections import deque

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, 'r') as f:
        return [(x) for x in f.read().split('\n')]

def get_pos(instructions: list) -> list:
    pos = [0, 0]
    directions = deque("ESWN")
    logging.debug(directions)
    for instruction in instructions:
        move, delta = instruction[:1], int(instruction[1:])
        if move in directions:
            pos = move_it(pos, move, delta)
        elif move in 'RL':
            directions = rotate(directions, move, delta)
            logging.debug(directions)
        else: # move == 'F'
            pos = move_it(pos, directions[0], delta)
    return abs(0 - pos[0]) + abs(0 - pos[1])


def get_pos_waypoint(instructions: list) -> list:
    pos = [0, 0]
    waypoint = [10, 1]
    directions = deque("ESWN")
    logging.debug(directions)
    for instruction in instructions:
        move, delta = instruction[:1], int(instruction[1:])
        if move in directions:
            waypoint = move_it(waypoint, move, delta)
        elif move in 'RL':
            waypoint = rotate_waypoint(waypoint, move, delta)
        else: # move == 'F'
            pos, waypoint = move_to_waypoint(pos, waypoint, delta)
    return abs(0 - pos[0]) + abs(0 - pos[1])

def move_to_waypoint(pos: list, waypoint: list, delta: int) -> list:
    count = 0
    while count < delta:
        pos = [pos[0] + waypoint[0], pos[1] + waypoint[1]]
        count = count + 1
    return pos, waypoint


def rotate_waypoint(waypoint: list, move: str, delta: int) -> list:
    if move == 'L': # assumes only 90 degree rotation, L270 == R90 and L90 == R270 and L180 == R180
        if delta == 90:
            delta = 270
        elif delta == 270:
            delta = 90
    if delta == 90:
        return [waypoint[1], -waypoint[0]]
    elif delta == 180:
        return [-waypoint[0], -waypoint[1]]
    else:
        return [-waypoint[1], waypoint[0]]


def rotate(directions: deque, move: str, delta: int) -> deque:
    logging.debug(f'enter rotate')
    logging.debug(f'{move} - {delta} - {int(delta/90)}')
    logging.debug(f'{directions}')
    rotation = int(delta/90)
    logging.debug(rotation)
    if move == 'R':
        directions.rotate(-rotation)
    else: # move == 'L'
        directions.rotate(rotation)

    logging.debug(f'{directions}')
    return directions


def move_it(pos: list, move: str, delta: int) -> list:
    logging.debug(f'entering move_it')
    logging.debug(f'{pos} - {move} - {delta}')
    if move == 'E':
        pos = [(pos[0] + delta), pos[1]]
    elif move == 'S':
        pos = [pos[0], (pos[1] - delta)]
    elif move == 'W':
        pos = [(pos[0] - delta), pos[1]]
    else: # move == 'N':
        pos = [pos[0], (pos[1] + delta)]

    logging.debug(f'{pos}')
    return pos



# def rotate_it(direction: deque, move: str, delta: int) -> list:

if __name__ == '__main__':
    # working_lst = clean_input('puzzle_input_test')
    working_lst = clean_input('puzzle_input')
    # working_lst = clean_input('puzzle_rotate_test')
    logging.info(f'answer for pt1: {get_pos(working_lst)}')
    logging.info(f'answer for pt2: {get_pos_waypoint(working_lst)}')
