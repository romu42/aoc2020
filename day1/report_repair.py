#!/usr/bin/env python3

# input is a list of numbers
# find two numbers that sum  2020, multiply these numbers for answer


def sum2020(data: list) -> int:
    report = [int(x) for x in data.readlines()]
    for i,num in enumerate(report):
        for i2, num2 in enumerate(report):
            for i3, num3 in enumerate(report):
                if (num + num2 + num3) == 2020 and i != i2 != i3:
                    return (num * num2 * num3)


if __name__ == '__main__':
    with open('puzzle_input') as data:
        print(sum2020(data))
