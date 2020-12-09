#!/usr/bin/env python3


""" 
    https://adventofcode.com/2020/day/7
    Luggage identified by color can contain varing amounts of other bags of color.
    You have a gold bag and you need to list out the number of bags that can contain your bag.

    example input: 

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    
"""

import logging, sys
from collections import defaultdict

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)

def parse_input_file(input) -> dict:
    luggage = {}
    with open(input) as f:
        lines = [x.strip() for x in f.read().split('.') if x != "\n"]
    for line in lines:
            logging.debug(f'  {line}')
            line = line.replace('bags', '').replace('bag', '').replace('no other', '0 color')
            #line = line.replace('bags', 'bag').replace('no other', '0 color')
            logging.debug(f'  {line}')
            bag, bags = line.split(' contain ')
            luggage[bag] = bags.split(' , ')

    #parsed_luggage = defaultdict(list)
    luggage_graph = defaultdict(list)
    luggage_parsed = defaultdict(dict)
    
    for key, value in luggage.items():
        key = key.strip()
        logging.debug(f'{key}-> {value}')
        for item in value:
            piece = item.split(" ", maxsplit=1)
            logging.debug(f'{piece[1].strip()}:{piece[0].strip()} ')
            luggage_parsed[key.strip()][piece[1].strip()] = int(piece[0])
            luggage_graph[key].append(piece[1].strip())

    #return parsed_luggage, luggage_graph
    return luggage_parsed, luggage_graph


def get_unique_bags(luggage: dict) -> list:
    unique_bags = []
    for bag, items in luggage.items():
        unique_bags.append(bag)
        logging.debug(f'   {bag} - {luggage[bag]}')
        for item in items:
            for slice in item:
                logging.debug(f'   {bag} - {slice}')
                unique_bags.append(slice.strip(' '))
        
    return set(unique_bags)    


def get_gold_carriers(luggage: dict, start: str, end: str, path=[]) -> list:
    lcnt = '--'
    logging.debug(f'{lcnt}-{path}-{(start)}-{(end)}')
    path = path + [start] 
    logging.debug(f'{lcnt}-{path}-{(start)}-{(end)}')
    if start == end:
        return path
    if start not in luggage:
        return
    #paths = []
    for node in luggage[start]:
        if node not in path:
            newpath = get_gold_carriers(luggage, node, end, path)
            if newpath: return newpath
            #for newpath in newpath:
            #    paths.append(newpath)
    #return f' the big return at the end'
    return

def get_goldbag_contents(luggage: dict, start: str, total: int):
    #for k,v in luggage.items():
        #print(f'{k} -- {v}')
    if luggage[start] == 0:
        return total
    print(start)
    node_cnt = 0
    for node in luggage[start]:
        if node == 'color':
            return 1
        print(f'{node} - {luggage[start][node]}')
        node_cnt = node_cnt + luggage[start][node]
        total = node_cnt * get_goldbag_contents(luggage, node, total)
    return total
    # lcnt = '--'
    # path = path + [start]
    # logging.info(f'{lcnt}-{path}-{(start)}-{(end)}')
    # if start == end:
    #     return path
    # if start not in luggage:
    #     return path
    # paths = []
    # for node in luggage[start]:
    #     if node not in path:
    #         newpaths = get_goldbag_contents(luggage, node, 'color', path)
    #         for newpath in newpaths:
    #             logging.info(f'{newpath}')
    #             paths.append(newpath)
    # return paths
#


if __name__ == '__main__':
    parsed_luggage, luggage_graph = parse_input_file('puzzle_input_test')
    parsed_luggage = dict(parsed_luggage)
    #parsed_luggage, luggage_graph = parse_input_file('puzzle_input')
    for k,v in parsed_luggage.items():
        logging.debug(f'{k}-{v}')
    for k,v in luggage_graph.items():
        logging.debug(f'{k}-{v}')
    #luggage = parse_input_file('puzzle_input')
    golden_carrier = [] 
    for bag in get_unique_bags(parsed_luggage):
        logging.debug(f'-{bag}-')
        bags = (get_gold_carriers(luggage_graph, bag, 'shiny gold'))
        if bags is not None:
            for bag in bags:
                golden_carrier.append(bag)
    print(len(set(golden_carrier))-1)
        
    print(get_goldbag_contents(parsed_luggage, 'shiny gold', 0))
