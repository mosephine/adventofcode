#! /usr/bin/python

import sys
from itertools import count

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

depart = int(lines[0])
busses = lines[1].split(',')

time = depart
my_bus = 0
for bus in busses:
    if bus == 'x':
        continue
    
    bus_int = int(bus)
    option = bus_int - (depart % bus_int)
    if option < time:
        time = option
        my_bus = bus_int

print("(Day 13, Part 1) wait time * bus line: %d" % (time * my_bus))

# part 2

bus_lines = []
for i in range(0, len(busses)):
    if busses[i].isdigit():
        bus_lines.append((int(busses[i]), i))

time, step = 0, 1
for bus, offs in bus_lines:
    for c in count(time, step):
        if (c + offs) % bus == 0:
            time, step = c, step * bus
            break

print("(Day 13, Part 2) earliest time when lines will fit departure constraints: %d" % time)

