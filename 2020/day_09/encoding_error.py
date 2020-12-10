#! /usr/bin/python

import sys

lines = [int(line.rstrip('\n')) for line in open(sys.argv[1])]
preamble = int(sys.argv[2])

def find_sum(space, needle):
    for i in range(0, len(space)):
        for j in range(i + 1, len(space)):
            if space[i] + space[j] == needle:
                return True

    return False

invalid = 0
for i in range(preamble, len(lines)):
    if find_sum(lines[i - preamble:i], lines[i]):
        continue
    else:
        invalid = lines[i]
        break

print("(Day 9, Part 1) first invalid number: %d" % (invalid))

nums = []
current_sum = 0
for i in range(0, len(lines) - 2):
    current_sum = lines[i]
    nums = [lines[i]]
    for j in range(i + 1, len(lines)):
        current_sum += lines[j]
        nums.append(lines[j])
        if current_sum < invalid:
            continue
        if current_sum >= invalid:
            break

    if current_sum == invalid:
        break

nums.sort()

print("(Day 9, Part 1) encryption weakness is: %d" % (nums[0] + nums[-1]))
