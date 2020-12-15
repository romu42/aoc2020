#!/usr/bin/env python3


from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import logging
import sys
from collections import defaultdict
import re

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.INFO)


mem = 'mem[42]'
# mask = [ x for x in '000000000000000000000000000000X1001X']
mem = 'mem[26]'
mask = [x for x in '00000000000000000000000000000000X0XX']
mem = re.findall(r'\d+', mem)
mem_place = int(mem[0])
logging.info((f'memory place = {mem_place:036b}'))
logging.debug(mask)
r = mask.count('X')
logging.debug(r)
indexes = [index for index, x in enumerate(mask) if x == 'X']
for index in indexes:
    logging.debug(mask[index])
logging.info(indexes)
# replacements = ['a', 'b']
replacements = ['0', '1']
# replacements = [replacement for replacement in combinations_with_replacement(replacements, r)]
# replacements = [replacement for replacement in permutations(replacements, r)]
replacements = [replacement for replacement in product(replacements, repeat=r)]
logging.info(replacements)
for group in replacements:
    for index, value in zip(indexes, group):
        logging.debug(f'{index}-{value}')
        mask[index] = value
    logging.info(f'{mask}')
    memory = "".join(mask)
    memory = int(memory)
    logging.info((f'{memory:036b}'))

