#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6

import re

def clean_input(incoming) -> list:
    with open(incoming) as f:
        lines = []
        line = ""
        group = 0
        for row in f:
            if re.match(r'^\s*$', row):
                    line = f'{group}-{line}'
                    lines.append(line)
                    line = ""
                    group = 0
            else:
                group = group + 1
                line += f'{row.strip()}'
        return lines

def get_answer_anyone(input) -> int:
    count = 0
    for line in input:
        group, answers = line.split('-')
        count = count + (len(set(answers)))
    return count


def get_answer_everyone(input) -> int:
    count = 0
    for line in input:
        group, answers = line.split('-')
        count = count + len([[x, answers.count(x)] for x in set(answers) if answers.count(x) == int(group)])
    return count

if __name__ == '__main__':

    #input = clean_input('puzzle_input_test')
    input = clean_input('puzzle_input')

    answer = get_answer_anyone(input)
    print(f'the magic number for anyone is : {answer}')

    answer = get_answer_everyone(input)
    print(f'the magic number for everyone is: {answer}')
    
         
