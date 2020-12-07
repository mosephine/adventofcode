#! /usr/bin/python

import sys

passes = [int(line.rstrip('\n').replace('F','0').replace('B','1').replace('L','0').replace('R','1'), 2) for line in open(sys.argv[1])]
passes.sort()

print("(Day 5, Part 1) highest seat id: %d" % (passes[-1]))

# find the missing seat
row_mask = int('1111111000', 2)
search = set([seat for seat in passes if seat in range ((passes[0] & row_mask) + 8, passes[-1] & row_mask)])
missing = (set([i for i in range(passes[0], passes[-1] + 1)]) - set(search)).pop()

print("(Day 5, Part 2) my seat id: %d" % (missing))
