#! /usr/bin/python

def reduce_polymer(fileobj, deletable):
    polymer = ""
    while True:
        ch = fileobj.read(1)
        if not ch or ch == '\n':
            # we've reached the end of the file
            fileobj.close()
            break

        if deletable and (ord(ch) == deletable or ord(ch) == deletable - 32): # added for part 2
            # don't use these polymers
            continue

        if not polymer:
            polymer += ch
            continue

        if abs(ord(ch) - ord(polymer[-1])) == 32:
            polymer = polymer[:-1]
        else:
            polymer += ch
    return polymer

# part 1: no special characters to remove
with open("input.txt") as fileobj:
    polymer = reduce_polymer(fileobj, None)
    print("(Day 5, Part 1) length of polymer: " + str(len(polymer)))

# part 2: shortest polymer with removed elements
shortest_polymer_len = 0

for item in range(ord('a'), ord('z')):
    with open("input.txt") as fileobj:
        polymer = reduce_polymer(fileobj, item)

        if shortest_polymer_len == 0 or shortest_polymer_len > len(polymer):
            shortest_polymer_len = len(polymer)

print("(Day 5, Part 2) length of shortest polymer: " + str(shortest_polymer_len))
