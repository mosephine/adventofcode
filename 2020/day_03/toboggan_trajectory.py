#! /usr/bin/python

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

# let's count some trees
def count_trees(slope_x, slope_y, matrix):
    pos_x = 0
    pos_y = 0
    len_x = len(matrix[0])
    len_y = len(matrix)

    trees = 0
    while pos_y < len_y:
        if matrix[pos_y][pos_x] == '#':
            trees += 1

        pos_y += slope_y
        pos_x = (pos_x + slope_x) % len_x

    return trees

trees = count_trees(3, 1, lines)
print("(Day 3, Part 1) number of trees hit on our way down: " + str(trees))

# slopes to check
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1
for slope in slopes:
    total *= count_trees(slope[0], slope[1], lines)

print("(Day 3, Part 2) product of trees hit on all slopes: " + str(total))
