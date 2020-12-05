#! /usr/bin/python

import re
import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

rule_re = re.compile("(\d+)-(\d+) (\w): (\w+)")
# parse input into passwords array
passwords = []
for line in lines:
    rule_match = rule_re.search(line)
    if rule_match:
        password = [int(rule_match.group(1)), int(rule_match.group(2)), rule_match.group(3), rule_match.group(4)]
        passwords.append(password)

# count the valid passwords according to Part 1 rules
valid_count = 0
for password in passwords:
    count = password[3].count(password[2])
    if count >= password[0] and count <= password[1]:
        valid_count += 1

print("(Day 2, Part 1) number of valid passwords: " + str(valid_count))

# count the valid passwords according to Part 2 rules
valid_count = 0
for password in passwords:
    found = False
    if password[2] == password[3][password[0] - 1]:
        found = True

    if len(password[3]) >= password[1]:
        if password[2] == password[3][password[1] - 1]:
            if not found:
                valid_count += 1
        elif found:
            valid_count += 1

print("(Day 2, Part 2) number of valid passwords: " + str(valid_count))
