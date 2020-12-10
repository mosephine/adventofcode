#! /usr/bin/python

import sys

jolts = [int(line.rstrip('\n')) for line in open(sys.argv[1])]

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts.sort()

ones = 0
threes = 0

diffs = []

for i in range(0, len(jolts) - 1):
    diff = jolts[i + 1] - jolts[i]
    diffs.append(diff)
    if diff == 1:
        ones += 1
    if diff == 3:
        threes += 1

print("(Day 10, Part 1) number of  ones * threes is: %d" % (ones * threes))

# part 2
#
# the only way to create additional combinations is by removing adapters.
# adapters with a difference of 3 from the previous cannot be removed
# so focus on ones with a difference of 1.
# 
# we only need to capture runs >= 2, because a single 1 cannot be removed.
runs = []
run = 0
for i in range(0, len(diffs)):
    if diffs[i] == 1:
        run += 1
    else:
        if run > 1:
            runs.append(run)
        run = 0

# the total combinations will be the product of the number of combinations
# for each run. the longest run is of 4 1's.
#
# len(run)  ->  combinations
# 2  -> 1 (nothing removed) + 1 (1 adapter removed) = 2
# 3  -> 1 (nothing removed) + 2 (1 adapter removed) + 1 (2 adapters removed) = 4
# 4  -> 1 (nothing removed) + 3 (1 adapter removed) + 3 (2 adapters removed) + 0 (3 adapters removed) = 7
combinations = 1
for run in runs:
    if run == 2:
        combinations = combinations * 2
    if run == 3:
        combinations = combinations * 4
    if run == 4:
        combinations = combinations * 7

print("(Day 10, Part 2) total combinations of adapters: %d" % (combinations))
