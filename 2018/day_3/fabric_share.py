#! /usr/bin/python
import re

lines = [line.rstrip('\n') for line in open('input.txt')]
regex = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

# parse lines into more easily manipulated data structure and
# find the bounding box for the fabric
max_width = 0
max_height = 0
terms = []

for line in lines:
    value = regex.search(line)
    name = int(value.group(1))
    x = int(value.group(2))
    y = int(value.group(3))
    w = int(value.group(4))
    h = int(value.group(5))
    terms.append([x, y, w, h, name])
    if x + w > max_width:
        max_width = x + w
    if y + h > max_height:
        max_height = y + h

# decompose the data into a matrix and determine which swatch has no overlap
bounds = [[[] for i in range(max_height)] for i in range(max_width)]
safe_swatch = set()
for term in terms:
    no_intersection = True
    for i in range (term[0], term[0] + term[2]):
        for j in range (term[1], term[1] + term[3]):
            if len(bounds[i][j]) > 0:
                no_intersection = False
                for item in bounds[i][j]:
                    safe_swatch.discard(item)
            bounds[i][j].append(term[4])
    if no_intersection:
        safe_swatch.add(term[4])

# count the number of squares with overlapping swatches
shared_squares = 0
for i in range(1, max_width):
    for j in range(1, max_height):
        if len(bounds[i][j]) > 1:
            shared_squares += 1

# return results
print("(Day 3, Part 1) shared fabric inches: " + str(shared_squares))
print("(Day 3, Part 2) safe fabric swatch: " + str(safe_swatch.pop()))
