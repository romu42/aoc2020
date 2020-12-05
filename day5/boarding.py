#!/usr/bin/env python3



def split_it(seat: str, v, list) -> list:
    pass

def get_seat(row: int, column: int) -> int:
    return row * 8 + column

if __name__ == '__main__':
    seats = []
    with open('puzzle_input') as f:
        tickets = [ x for x in f ]
    for ticket in tickets:
        rows = ticket[0:7]
        columns = ticket[7:10]
        r_seats = [x for x in range(0,128)]
        c_seats = [x for x in range(0,8)]
        
        for slicer in rows:
            if slicer == 'B':
#                print(f'slicer is {slicer}')
                r_seats = (r_seats[int(len(r_seats)/2):])
#                print(r_seats)
            else:
#                print(f'slicer is {slicer}')
                r_seats = (r_seats[:int(len(r_seats)/2)])
#                print(r_seats)
            row = int(r_seats[0])
            
        for slicer in columns:
#            print(columns)
#            print(c_seats)
            if slicer == 'R':
#                print(f'slicer is {slicer}')
                c_seats = (c_seats[int(len(c_seats)/2):])
#                print(c_seats)
            else:
#                print(f'slicer is {slicer}')
                c_seats = (c_seats[:int(len(c_seats)/2)])
#                print(c_seats)
            column = int(c_seats[0])
    
        seats.append(get_seat(row, column))
    #for seat in seats:
        #print(f'seat id: {seat}')
    print(f'The highest boarding card is: {max(seats)}')
    seats.sort()
    for i, seat in enumerate(seats):
        try:
            if seats[i+1] - seats[i] > 1:
                print(f'Sir your seat will be: {seat+1}')
        except IndexError:
            print(f'ran out of elements in the list')
