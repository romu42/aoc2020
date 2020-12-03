#!/usr/bin/env python3


def define_hill(file) -> list:
    with open(file) as f:
        return [x.strip() for x in f.readlines()]
    

def get_tree_count(right: int, down: int, hill: list) -> int:
    width = len(hill[0])
    row = 0
    tree_count = 0
    for point in hill[0::down]:
        posistion = row * right
        if point[posistion % width] == "#":
            tree_count = tree_count + 1
        row = row + 1
    return tree_count


if __name__ == '__main__':
    hill = define_hill("puzzle_input")
    slopes = [
            [1,1],
            [3,1],
            [5,1],
            [7,1],
            [1,2],
            ]
    total_trees = 1
    for slope in slopes:
        trees = (get_tree_count(slope[0], slope[1], hill))
        total_trees = total_trees * trees
    print(total_trees)
