#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6

import re

def clean_input(incoming) -> list:
    with open(incoming) as f:
        lines = []
        line = ""
        for row in f:
            if re.match(r'^\s*$', row):
                    lines.append(line)
                    line = ""
            else:
                line += f'{row.strip()}'
        return lines


if __name__ == '__main__':

    #input = clean_input('puzzle_input_test')
    input = clean_input('puzzle_input')
    
    count = 0
    for line in input:
        count = count + (len(set(line)))
         
    print(f'the magic number is: {count}')
