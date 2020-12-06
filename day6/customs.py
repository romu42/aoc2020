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
        count = count + len([x for x in set(answers) if answers.count(x) == int(group)])
    return count


def get_answer_anyone2(incoming) -> int:
    with open(incoming) as f:
        lines = f.read().split("\n\n")
        return sum([len(set(x.replace("\n", ""))) for x in lines])


def get_answer_everyone2(incoming) -> int:
    with open(incoming) as f:
        lines = f.read().split("\n\n")
        listan = ([[y for y in set(x) if x.count(y) == x.count("\n") + 1] for x in lines])
        count = 0
        for row in listan:
            count = count + len(row)
        return count
    


if __name__ == '__main__':

    # fist attempt with some cludgy input clean up
    #input = clean_input('puzzle_input_test')
    input = clean_input('puzzle_input')

    answer = get_answer_anyone(input)
    print(f'the magic number for anyone is : {answer}')

    answer = get_answer_everyone(input)
    print(f'the magic number for everyone is: {answer}')
   

    # Second attemt with some cleaner input handling thanks to https://github.com/bombsimon
    print(get_answer_anyone2('puzzle_input'))
    print(get_answer_everyone2('puzzle_input'))

