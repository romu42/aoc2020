#!/usr/bin/env python3

import logging
import sys
from collections import deque

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format="  %(message)s  ", stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, "r") as f:
        input_list = []
        # line = [[x for x in x.split(" ")] for x in f.read().split("\n")]
        for line in f.read().split("\n"):
            # line = [int(x) if x.isdigit() else x for x in line.split(" ")]
            input_list.append(line)
        return input_list


def reverse_precedence(expression: str) -> int:
    adds = [x for x in expression.split(" * ")]
    logging.info(adds)
    add_parts = [sum(int(x) for x in part if x.isdigit()) for part in adds]
    total = 1
    for num in add_parts:
        total *= num
    return total


def left_to_right(expression: list) -> int:
    parts = deque([x for x in expression if x != " "])
    evaluate = []
    while len(parts) >= 3:
        while len(evaluate) < 3:
            evaluate.append(parts.popleft())
        if evaluate[1] == "+":
            parts.appendleft(int(evaluate[0]) + int(evaluate[2]))
        else:
            parts.appendleft(int(evaluate[0]) * int(evaluate[2]))
        evaluate = []
    return parts


def strip_para(expression: list):
    expression = [x for x in expression]
    local_list = []
    if "(" not in expression:
        return left_to_right(expression)
    for count, value in enumerate(expression):
        if value != "(" and value != ")":
            local_list.append(value)
        elif value == "(":
            place = count + 1
            strip_para(expression[place:])
        else:
            part_answer = left_to_right(local_list)
            expression[0 : count + 1] = list(part_answer)
    return expression

    return local_list


if __name__ == "__main__":
    working_lst = clean_input("puzzle_input_test")
    # working_lst = clean_input('puzzle_input')
    for item in working_lst:
        item = item.replace("(", "( ")
        item = item.replace(")", " )")
        expression = []
        item_total = strip_para(item)
        logging.info(left_to_right(item_total))
        # logging.info(item_total)
