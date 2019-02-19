#! /usr/bin/python

grid = [list(line.rstrip('\n')) for line in open('data.in')]
width = len(grid[0])
replace = {'.': 0, '|': 1, '#': 10}
prev_grid = [[replace.get(n,n) for n in grid[i]] for i in range(width)]

# '.' -> '|' if '|' > 2
# '|' -> '#' if '#' > 2
# '#' -> '#' if '#' > 0 && '|' > 0 else '#' -> '.'

resource_value = 0
for i in range(0, 1000000000):
    next_grid = [[0 for n in range(width)] for m in range(width)]
    n_trees = 0
    n_yards = 0

    for j in range(0, width):
        for k in range(0, width):
            total = 0
            trees = 0
            yards = 0
            if j > 0:
                total += prev_grid[j-1][k]
                if k > 0:
                    total += prev_grid[j-1][k-1]
                if k < width - 1:
                    total += prev_grid[j-1][k+1]
            if k > 0:
                total += prev_grid[j][k-1]
                if j < width - 1:
                    total += prev_grid[j+1][k-1]
            if j < width - 1:
                total += prev_grid[j+1][k]
                if k < width - 1:
                    total += prev_grid[j+1][k+1]
            if k < width - 1:
                total += prev_grid[j][k+1]

            trees = total % 10
            yards = total // 10
            if prev_grid[j][k] == 0:
                if trees > 2:
                    next_grid[j][k] = 1
                    n_trees += 1
            elif prev_grid[j][k] == 1:
                if yards > 2:
                    next_grid[j][k] = 10
                    n_yards += 1
                else:
                    next_grid[j][k] = 1
                    n_trees += 1
            elif trees > 0 and yards > 0:
                next_grid[j][k] = 10
                n_yards += 1

    new_rv = n_trees * n_yards
    if resource_value == new_rv:
        break
    resource_value = new_rv
    prev_grid = next_grid

print('(Day 18, Part 1) total resource value: ' + str(resource_value))
