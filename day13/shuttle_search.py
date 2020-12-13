#!/usr/bin/env python3

import logging
import sys
from collections import deque

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, 'r') as f:
        return [x for x in f.read().split('\n')]


def next_available_bus(departures: list):
    time_table = {}
    earliest_departure = int(departures[0])
    departures = departures[1]
    departures = [int(x) for x in departures.split(',') if x != 'x']
    for bus_id in departures:
        delta = earliest_departure % bus_id
        next_arrival = (earliest_departure - delta) + bus_id
        time_to_arrival = next_arrival - earliest_departure
        time_table[bus_id] = time_to_arrival
    next_bus = min(time_table, key=lambda x: time_table[x])
    logging.info(f'time to next departing bus {time_table[next_bus]} with id {next_bus}')
    logging.info(f'answer to pt1: {time_table[next_bus] * next_bus}')


def timestamp(bus_ids: list):
    modifier_table = {}
    bus_ids = bus_ids[1].split(',')
    bus1 = int(bus_ids[0])

    for modifier, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            modifier_table[int(bus_id)] = modifier
    logging.info(len(modifier_table))
    time = 0
    magic_number = len(modifier_table)
    big_bus = max(modifier_table, key=lambda x: modifier_table[x])
    logging.info(f'the big_bus is {big_bus} with modifier {modifier_table[big_bus]}')
    while True:
        time = time + bus1
        # time = time + big_bus - modifier_table[big_bus]
        counter = 0
        for bus_id, modifier in modifier_table.items():
            if (time + modifier) % bus_id == 0:
                counter = counter + 1
            else:
                next
        if counter == magic_number:
            logging.info(f'the timestamp needed is {time}')
            break

if __name__ == '__main__':
    # working_lst = clean_input('puzzle_input_test')
    working_lst = clean_input('puzzle_input')
    # working_lst = ['bob', '17,x,13,19']
    # working_lst = ['bob', '67,7,59,61']
    # working_lst = ['bob', '67,x,7,59,61']
    # working_lst = ['bob', '67,7,x,59,61']
    # working_lst = ['bob', '1789,37,47,1889']
    # for row in working_lst:
    #     logging.info(row)

    # next_available_bus(working_lst)
    timestamp(working_lst)