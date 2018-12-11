#! /usr/bin/python

lines = [line.rstrip('\n') for line in open('input.txt')]

n_twos = 0
n_threes = 0

for line in lines:
    line = sorted(line)
    for i in range(0, len(line) - 1):
        if line[i] == line[i+1]:
            n_twos += 1
            break
    for i in range(0, len(line) - 2):
        if line[i] == line[i+2]:
            n_threes += 1
            break

print("(Day 2, Part 1) checksum: " + str(n_twos * n_threes))

end_reached = False
for line1 in lines:
    for line2 in lines:
        errors_detected = 0
        for i in range(0, len(line1)):
            if line1[i] == line2[i]:
                continue

            errors_detected += 1
        if errors_detected == 1:
            intersection = ""
            for i in range(0, len(line1)):
                if line1[i] == line2[i]:
                    intersection += line1[i]
            print("(Day 2, Part 2) common letters: " + intersection)
            end_reached = True
            break
    if end_reached:
        break
