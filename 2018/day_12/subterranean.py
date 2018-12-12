#! /usr/bin/python

import re

lines = [line.rstrip('\n') for line in open('input.txt')]

seed = re.search("initial state: ([\.\#]+)", lines[0]).group(1)
lines = lines[2:]
rules = []

rules_re = re.compile("^([\.\#]{5}) => ([\.\#])$")

indices = [i for i in range(-5, 300)]
def transform_value(line):
    global indices
    value = 0
    for i in range(0, len(line)):
        if line[i] == '#':
            value += indices[i]

    return value


for line in lines:
    rule_re = rules_re.search(line)
    rule = re.escape(rule_re.group(1))
    transform = rule_re.group(2)
    if rule[2] != transform[0]:
        rules.append((re.compile("(" + rule + ")"), transform, rule))

transforms = []
prev_generation = "....." + seed + "."*110
prev_value = transform_value(prev_generation)
prev_difference = 0
part1_answer = 0
generation = 0

for i in range(0, 101):
    #print(prev_generation)
    transforms.append(prev_generation)
    new_generation = ""

    # for our check, we need to pad the generation with empty pots
    check = ".." + prev_generation + ".."
    for j in range(2, len(check) - 2):
        unchanged = True
        for rule in rules:
            match = rule[0].search(check[j-2:j+3])
            if match:
                new_generation += rule[1]
                unchanged = False
                break
        if unchanged:
            new_generation += "."

    # check transform value as we go
    new_value = transform_value(new_generation)
    if i == 19:
        part1_answer = new_value

    new_difference = new_value - prev_value
    if new_difference == prev_difference:
        # we've reached a stable generation, we can stop now
        generation = i + 1
        break

    prev_value = new_value
    prev_difference = new_difference
    prev_generation = new_generation


billions = new_value + (new_difference * (50000000000 - generation))

print("(Day 12, Part 1) total value for plants after 20 generations: " + str(part1_answer))
print("(Day 12, Part 2) total value for plants after 5 billion generations: " + str(billions))
