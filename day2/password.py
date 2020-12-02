#!/usr/bin/env python3



if __name__ == "__main__":
    counter = 0
    with open("puzzle_input") as f:
        password_list = [ x.strip() for x in f.readlines()]
    for line in password_list:
        count, letter, password = line.split()
        low, high = count.split('-')
        low, high = int(low)-1, int(high)-1 # an ugly hack since index is 1
        letter = str(letter.strip(':'))
        #if low <= password.count(letter) <= high:
        #    counter = counter + 1
        if (password[low] == letter or password[high] == letter):
            if (password[low] != password[high]):
                counter = counter + 1

    print(counter)
