#!/usr/bin/env python3

import re


def clean_input(file) -> list:
    id = ""
    list_of_ids = []
    with open(file) as f:
        inputs = ([x.strip() for x in f])
    for line in inputs:
        if re.match(r'^\s*$', line):
            list_of_ids.append(id)
            id = ""
        else:
            id += f'{line} '
    return list_of_ids


def check_valid(id: str) -> bool:
    if id.count(':') == 8 or id.count(':') == 7 and 'cid:' not in id:
        return True


def check_super_valid(id: str) -> bool:
    debug = ""
    for entry in id.split(' '):
        k,v = entry.split(':')
        if k == 'pid':
            if re.fullmatch(r'[0-9]{9}', v):
                next
            else:
                return False
        elif k == 'byr':
            if re.fullmatch(r'[0-9]{4}', v) and (1920 <= int(v) <= 2002):
                next
            else:
                return False
        elif k == 'eyr': 
            if re.fullmatch(r'[0-9]{4}', v) and (2020 <= int(v) <= 2030):
                next
            else:
                return False
        elif k == 'iyr':
            if re.fullmatch(r'[0-9]{4}', v) and (2010 <= int(v) <= 2020):
                next
            else:
                return False
        elif k == 'hgt':
            if 'cm' in v:
                height = v.strip('cm')
                if re.fullmatch(r'[0-9]{3}', height) and (150 <= int(height) <= 193):
                    next
                else:
                    return False
            elif 'in' in v:
                height = v.strip('in')
                if re.fullmatch(r'[0-9]{2}', height ) and (59 <= int(height) <= 76):
                    next
                else:
                    return False
            else:
                return False
        elif k == 'hcl':
            if re.fullmatch(r'\#[0-9a-f]{6}', v):
                next
            else:
                return False
        elif k == 'ecl':
            if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                next
            else:
                return False 
        elif k == 'cid':
            next    
    return True           

    

if __name__ == '__main__':
    valid_identification = 0
    super_valid = 0
#    id_list = clean_input("puzzle_input_test")
    id_list = clean_input("puzzle_input")
    for id in id_list:
       check = check_valid(id)
       if check:
           valid_identification = valid_identification + 1
           if check_super_valid(id.strip(' ')):
               super_valid = super_valid + 1

    print(f'number of valid identifications :{valid_identification}')
    print(f'number of super valid is : {super_valid}')

