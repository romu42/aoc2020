#!/usr/bin/env python3
# https://adventofcode.com/2020/day/5



def slice_it(seat: str, seats: list) -> list:
    for slicer in seat:
        if slicer == 'B' or slicer == 'R':
            seats = (seats[int(len(seats)/2):])
        else:
            seats = (seats[:int(len(seats)/2)])
    return int(seats[0])


def get_seat(row: int, column: int) -> int:
    return row * 8 + column


if __name__ == '__main__':
    seats = []
    with open('puzzle_input') as f:
        tickets = [ x for x in f ]
    for ticket in tickets:
        row = slice_it(ticket[0:7], [x for x in range(0,128)])
        column = slice_it(ticket[7:10], [x for x in range(0,8)])
        seats.append(get_seat(row, column))
    print(f'The highest boarding card is: {max(seats)}')
    
    seats.sort()
    for i, seat in enumerate(seats):
        try:
            if seats[i+1] - seats[i] > 1:
                print(f'Sir your seat will be: {seat+1}')
        except IndexError:
            print(f'ran out of elements in the list')
