#! /usr/bin/python

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

ordinals = ['E', 'S', 'W', 'N']
turns = {90: 1, 180: 2, 270: 3}

direction = 0
position = (0, 0)
for line in lines:
    d = line[0]
    amount = int(line[1:])

    if d == 'L':
        direction = (direction - turns[amount]) % 4
    if d == 'R':
        direction = (direction + turns[amount]) % 4

    if d == 'E' or (d == 'F' and ordinals[direction] == 'E'):
        position = (position[0] + amount, position[1])
    if d == 'W' or (d == 'F' and ordinals[direction] == 'W'):
        position = (position[0] - amount, position[1])
    if d == 'N' or (d == 'F' and ordinals[direction] == 'N'):
        position = (position[0], position[1] + amount)
    if d == 'S' or (d == 'F' and ordinals[direction] == 'S'):
        position = (position[0], position[1] - amount)

print("(Day 12, Part 1) Manhattan Distance from start to end points: %d" % (abs(position[0]) + abs(position[1])))

# for part 2, only the F instruction moves the actual ferry position, everything else moves the waypoint

waypoint = (10, 1)
direction = 0
ferry = (0, 0)

for line in lines:
    d = line[0]
    amount = int(line[1:])

    if d == 'F':
        ferry = (ferry[0] + (waypoint[0] * amount), ferry[1] + (waypoint[1] * amount))

    if d == 'E':
        waypoint = (waypoint[0] + amount, waypoint[1])
    if d == 'W':
        waypoint = (waypoint[0] - amount, waypoint[1])
    if d == 'N':
        waypoint = (waypoint[0], waypoint[1] + amount)
    if d == 'S':
        waypoint = (waypoint[0], waypoint[1] - amount)

    # this part is more complex :/
    if (d == 'L' and amount == 90) or (d == 'R' and amount == 270):
        waypoint = (waypoint[1] * -1, waypoint[0])
    if (d == 'L' and amount == 180) or (d == 'R' and amount == 180):
        waypoint = (waypoint[0] * -1, waypoint[1] * -1)
    if (d == 'L' and amount == 270) or (d == 'R' and amount == 90):
        waypoint = (waypoint[1], waypoint[0] * -1)


print("(Day 12, Part 2) Manhattan Distance from start to end points (using waypoint): %d" % (abs(ferry[0]) + abs(ferry[1])))
