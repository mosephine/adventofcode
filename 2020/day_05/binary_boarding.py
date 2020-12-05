#! /usr/bin/python

import sys

passes = [int(line.rstrip('\n').replace('F','0').replace('B','1').replace('L','0').replace('R','1'), 2) for line in open(sys.argv[1])]
passes.sort()

print("(Day 5, Part 1) highest seat id: %d" % (passes[-1]))

# find the missing seat
search = set([i for i in passes if i in range (9, passes[-1] & int('1111111000', 2))])
missing = set([i for i in range(passes[0], passes[-1] + 1)]) - set(search)
boarding_pass = missing.pop()

print("(Day 5, Part 2) my seat id: %d" % (boarding_pass))
