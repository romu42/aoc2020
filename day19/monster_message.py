#!/usr/bin/env python3

import logging
import sys
from collections import deque

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format="  %(message)s  ", stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, "r") as f:
        r = []
        v = []
        for x in f.read().split("\n"):
            if x[0].isdigit():
                r.append(x)
            else:
                v.append(x)
        return r, v


def organize_rules(r: list) -> dict:
    r.sort()
    rulez = {}
    for item in r:
        k, v = item.split(":")
        rulez[k] = v
    for k, v in rulez.items():
        print(f"key: {k} has value:{v}")


if __name__ == "__main__":
    # rules, values = clean_input("puzzle_input_test")
    rules, values = clean_input("puzzle_input")
    organize_rules(rules)
