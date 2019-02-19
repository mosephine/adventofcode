#! /usr/bin/python

routes = [list(line.rstrip('\n')) for line in open('data.in')]

directions = ['<', 'v', '>', '^']
tracks = ['|', '-', '/', '\\', '+']

# cart tuples = (position, direction, n_intersections)
# e.g. a cart at position (1,2) facing left and having
# seen 3 intersections = ((1,2), '<', 3)
carts = []
for y in range(len(routes)):
    for x in range(len(routes[0])):
        if routes[y][x] in directions:
            cart = ((x,y), routes[y][x], 0)
            routes[y][x] = '-' if routes[y][x] in ['<', '>'] else '|'
            carts.append(cart)

moves = {
        ('/' , '<') : 'v',
        ('/' , '^') : '>',
        ('/' , '>') : '^',
        ('/' , 'v') : '<',
        ('\\', '<') : '^',
        ('\\', '^') : '<',
        ('\\', '>') : 'v',
        ('\\', 'v') : '>'
        }

positions = {
        '<': (-1, 0),
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1)
        }

part1 = None
part2 = None
crash = None
while True:
    carts = sorted(carts)
    new_carts = []
    while carts:
        cart = carts[0]
        carts = carts[1:]
        # update each cart position until a crash
        current_track = routes[cart[0][1]][cart[0][0]]
        next_direction = cart[1]
        next_int_count = cart[2]
        if current_track in ['/', '\\']:
            next_direction = moves[(current_track, cart[1])]
        elif current_track == '+':
            select = next_int_count % 3
            if select == 0:
                next_direction = directions[(directions.index(cart[1]) + 1) % 4]
            elif select == 2:
                next_direction = directions[(directions.index(cart[1]) + 3) % 4]
            next_int_count += 1

        next_position = (cart[0][0] + positions[next_direction][0], cart[0][1] + positions[next_direction][1])

        # check for collision in carts and new_carts
        check = [x for x in carts]
        check.extend(new_carts)
        crash = [x[0] for x in check if x[0] == next_position]
        if crash:
            crash = crash[0]
            if not part1:
                part1 = crash
            # remove crashed carts and keep going
            carts = [x for x in carts if x[0] != next_position]
            new_carts = [x for x in new_carts if x[0] != next_position]
        else:
            new_carts.append((next_position, next_direction, next_int_count))

    if len(new_carts) == 1:
        part2 = new_carts[0][0]
        break
    carts = new_carts


print("(Day 13, Part 1): first crash intersection: " + str(part1[0]) + "," + str(part1[1]))
if part2:
    print("(Day 13, Part 2): last remaining cart position: " + str(part2[0]) + "," + str(part2[1]))
