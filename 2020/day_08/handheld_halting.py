#! /usr/bin/python

import sys

instructs = [line.rstrip('\n').split(' ') for line in open(sys.argv[1])]

for instruct in instructs:
    instruct[1] = int(instruct[1])
    instruct.append(False)
    instruct.append(False)

def clear(instructs):
    for instruct in instructs:
        instruct[2] = False

def run(instructs, part1=True):
    accum = 0
    i = 0
    swapped = False
    while i in range(0, len(instructs)):
        if instructs[i][2]:
            if part1:
                break
            else:
                i = 0
                accum = 0
                clear(instructs)
                swapped = False
                continue

        instructs[i][2] = True
        if instructs[i][0] == "acc":
            accum += instructs[i][1]
            i += 1
            continue

        inst = instructs[i][0]
        if not part1:
            if not instructs[i][3] and not swapped:
                if inst == "jmp":
                    inst = "nop"
                else:
                    inst = "jmp"
                instructs[i][3] = True
                swapped = True

        if inst == "jmp":
            i += instructs[i][1]
            continue

        if inst == "nop":
            i += 1
            continue

    return accum

print("(Day 8, Part 1) ammount in accumulator before loop: %d" % (run(instructs)))
print("(Day 8, Part 1) ammount in accumulator once loop is broken: %d" % (run(instructs, False)))
