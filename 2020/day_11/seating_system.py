#! /usr/bin/python

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

rows = len(lines)
columns = len(lines[0])

def run_round1(grid):
    new_grid = []
    changed = False
    for r in range(0, rows):
        new_grid.append([])
        for c in range(0, columns):
            if grid[r][c] == '.':
                new_grid[r].append('.')
                continue

            n_occupied = 0
            if not c == (columns - 1):
                if grid[r][c+1] == '#':
                    n_occupied += 1
                if not r == (rows - 1) and grid[r+1][c+1] == '#':
                    n_occupied += 1
                if r and grid[r-1][c+1] == '#':
                    n_occupied += 1


            if c:
                if grid[r][c-1] == '#':
                    n_occupied += 1
                if not r == (rows - 1) and grid[r+1][c-1] == '#':
                    n_occupied += 1
                if r and grid[r-1][c-1] == '#':
                    n_occupied += 1

                
            if not r == (rows - 1):
                if grid[r+1][c] == '#':
                    n_occupied += 1
            if r:
                if grid[r-1][c] == '#':
                    n_occupied += 1

            if grid[r][c] == '#' and n_occupied > 3:
                new_grid[r].append('L')
                changed = True
            elif grid[r][c] == 'L' and n_occupied == 0:
                new_grid[r].append('#')
                changed = True
            else:
                new_grid[r].append(grid[r][c])

    return (changed, new_grid)

changed, new_grid = run_round1(lines)
while changed:
    changed, new_grid = run_round1(new_grid)

n_occupied = 0
for row in new_grid:
    for char in row:
        if char == '#':
            n_occupied += 1

print("(Day 11, Part 1) number of occupied seats using part 1 rules: %d" % (n_occupied))

# part 2 - classic solution would memoize, which I suck at
grids = [lines]

def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

# directions are: lt, rt, up, dn, lu, ru, ld, rd

@memoize
def seats(params):
    global rows
    global columns
    global grids
    occupied = False
    r = params[0]
    c = params[1]
    direction = params[2]
    grid = grids[params[3]]
    new_r = r
    new_c = c
    valid = False
    if direction == 'lt':
        if c:
            new_c = c - 1
            valid = True
    if direction == 'rt':
        if not c == (columns -1):
            new_c = c + 1
            valid = True
    if direction == 'up':
        if r:
            new_r = r - 1
            valid = True
    if direction == 'dn':
        if not r == (rows - 1):
            new_r = r + 1
            valid = True
    if direction == 'lu':
        if c and r:
            new_r = r - 1
            new_c = c - 1
            valid = True
    if direction == 'ru':
        if not c == (columns - 1) and r:
            new_r = r - 1
            new_c = c + 1
            valid = True
    if direction == 'ld':
        if c and not r == (rows - 1):
            new_r = r + 1
            new_c = c - 1
            valid = True
    if direction == 'rd':
        if not c == (columns - 1) and not r == (rows - 1):
            new_r = r + 1
            new_c = c + 1
            valid = True
    
    if not valid:
        return 0

    if grid[new_r][new_c] == '#':
        occupied = True
    elif grid[new_r][new_c] == 'L':
        occupied = False
    else:
        occupied = seats((new_r, new_c, direction, params[3]))

    return occupied


def run_round2(grid, step):
    new_grid = []
    changed = False
    for r in range(0, rows):
        new_grid.append([])
        for c in range(0, columns):
            n_occupied = 0

            if seats((r, c, 'lt', step)):
                n_occupied += 1
            if seats((r, c, 'rt', step)):
                n_occupied += 1
            if seats((r, c, 'up', step)):
                n_occupied += 1
            if seats((r, c, 'dn', step)):
                n_occupied += 1
            if seats((r, c, 'lu', step)):
                n_occupied += 1
            if seats((r, c, 'ld', step)):
                n_occupied += 1
            if seats((r, c, 'ru', step)):
                n_occupied += 1
            if seats((r, c, 'rd', step)):
                n_occupied += 1
             
            if grid[r][c] == '#' and n_occupied > 4:
                new_grid[r].append('L')
                changed = True
            elif grid[r][c] == 'L' and n_occupied == 0:
                new_grid[r].append('#')
                changed = True
            else:
                new_grid[r].append(grid[r][c])

    return changed, new_grid


step = 0
changed, new_grid = run_round2(lines, step)
while changed:
    step += 1
    grids.append(new_grid)
    changed, new_grid = run_round2(new_grid, step)

n_occupied = 0
for row in new_grid:
    for char in row:
        if char == '#':
            n_occupied += 1

print("(Day 11, Part 2) number of occupied seats using part 2 rules: %d" % (n_occupied))

