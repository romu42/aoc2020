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
