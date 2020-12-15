#! /usr/bin/python

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]
numbers = [int(l) for l in lines[0].split(',')]

# not the most efficient algorithm, but gets the job done
def get_nth(nums, n):
    turn = 1
    game = {}
    last = 0

    for num in nums:
        last = num
        game[last] = [turn]
        turn += 1

    while turn <= n:
        age = 0
        if len(game[last]) == 1 and game[last][-1] == (turn - 1):
            age = 0
        else:
            age = game[last][-1] - game[last][-2]

        if age in game:
            game[age].append(turn)
        else:
            game[age] = [turn]

        last = age
        turn += 1

    return last

print("(Day 15, Part 1) 2020th number in game: %d" % get_nth(numbers, 2020))
print("(Day 15, Part 2) 30000000th number in game: %d" % get_nth(numbers, 30000000))
