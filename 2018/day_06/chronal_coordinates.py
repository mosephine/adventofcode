#! /usr/bin/python

from collections import Counter

coords = [tuple(map(int, line.strip().split(','))) for line in open('input.txt')]

# determine grid size
x_max = max(x[0] for x in coords)
y_max = max(y[1] for y in coords)

# calculate minimum manhattan distance between nodes
grid = {}
for i in range(x_max):
    for j in range(y_max):
        m = min(abs(i - k) + abs(j - l) for k, l in coords)
        for n, (k, l) in enumerate(coords):
            if abs(i - k) + abs(j - l) == m:
                if grid.get((i, j), -1) != -1:
                    grid[(i, j)] = -1
                    break
                grid[(i, j)] = n

# exclude infinite regions 
s = set([-1])
s = s.union(set(grid[x, y_max - 1] for x in range(x_max)))
s = s.union(set(grid[x,         0] for x in range(x_max)))
s = s.union(set(grid[x_max - 1, y] for y in range(y_max)))
s = s.union(set(grid[        0, y] for y in range(y_max)))

largest_area = next(i[1] for i in Counter(grid.values()).most_common() if i[0] not in s)
print("(Day 6, Part 1) largest finite area: " + str(largest_area))

largest_region = sum(sum(abs(i - k) + abs(j - l) for k, l in coords) < 10000 
        for i in range(x_max) for j in range(y_max))
print("(Day 6, Part 2) largest region < 10000: " + str(largest_region))
