#! /usr/bin/python

lines = [line.rstrip('\n') for line in open('input.txt')]

total = 0
for line in lines:
    total += int(line)
print("(Day 1, Part 1) final frequency: " + str(total))

total = 0
totals = {}
still_trying = True
while still_trying:
    for line in lines:
        total += int(line)
        if total in totals:
            still_trying = False
            break
        totals[total] = 1
print("(Day 1, Part 2) first frequency reached twice: " + str(total))
