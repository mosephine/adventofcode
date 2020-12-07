#! /usr/bin/python

import sys
from itertools import groupby

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

yeses = 0
forms = []
form = set()
for line in lines:
    if not line:
        yeses += len(form)
        forms.append(form)
        form = set()
        continue
    for item in line:
        form.add(item)
yeses += len(form)
forms.append(form)

print("(Day 6, Part 1) total yes answers: %d" % (yeses))

forms = [list(group) for key, group in groupby(lines, lambda x: not x) if not key]
yeses = 0
for form in forms:
    final = set(form[0])
    for person in range(1, len(form)):
        final = final.intersection(set(form[person]))
    yeses += len(final)

print("(Day 6, Part 2) total yes answers: %d" % (yeses))
