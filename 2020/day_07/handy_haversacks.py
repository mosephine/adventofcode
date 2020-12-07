#! /usr/bin/python

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

contained_tree = {}
contains_tree = {}
for line in lines:
    chunks = line.split(" bags contain ")
    contains = chunks[0]
    contained = chunks[1].rstrip('.').split(", ")
    for bag in contained:
        tokens = bag.split(' ')
        if tokens[0].isdigit():
            desc = tokens[1] + " " + tokens[2]
        else:
            desc = "no other"

        if desc in contained_tree:
            contained_tree[desc].append(contains)
        else:
            contained_tree[desc] = [contains]

        if tokens[0].isdigit():
            if contains in contains_tree:
                contains_tree[contains].append([desc, tokens[0]])
            else:
                contains_tree[contains] = [[desc, tokens[0]]]

# we're looking for all the bags that could eventually contain a shiny gold bag

def add_bags(tree, key):
    if key not in tree:
        return set()

    containers = set()
    for bag in tree[key]:
        containers.add(bag)
        containers |= add_bags(tree, bag)

    return containers

containers = add_bags(contained_tree, "shiny gold")
print("(Day 7, Part 1) number of bags that count eventually contain a shiny gold bag: %d" % (len(containers)))

# we're looking for the total of all bags that would be contained in a shiny gold bag

def count_bags(tree, key):
    if key not in tree:
        return 1
    
    count = 1
    for bag in tree[key]:
        count += int(bag[1]) * count_bags(tree, bag[0])

    return count

count = count_bags(contains_tree, "shiny gold")
print("(Day 7, Part 2) number of bags contained in a shiny gold bag: %d" % (count - 1))
