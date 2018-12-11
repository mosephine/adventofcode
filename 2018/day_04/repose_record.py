#! /usr/bin/python

import re

lines = [line.rstrip('\n') for line in open('input.txt')]

# sort lines into time order
lines = sorted(lines)

# compile regex for each type of line
start_re = re.compile("\[.+\] Guard #(\d+) begins shift")
sleep_re = re.compile("\[\d{4}\-\d\d\-\d\d \d\d\:(\d\d)\] falls asleep")
wake_re = re.compile("\[\d{4}\-\d\d\-\d\d \d\d\:(\d\d)\] wakes up")

# initialize hash of guards
guards_totals = {}
guards_ranges = {}

# for each shift, tally the minutes a guard slept
index = 0
while index < len(lines):
    match_guard = start_re.search(lines[index])
    if match_guard:
        guard_id = match_guard.group(1)
        if guard_id not in guards_totals:
            guards_totals[guard_id] = 0
            guards_ranges[guard_id] = []
        index += 1
        while index < len(lines) and not start_re.search(lines[index]):
            start_time = 0
            end_time = 0
            match_sleep = sleep_re.search(lines[index])
            if match_sleep:
                start_time = int(match_sleep.group(1))
                end_time = start_time
            index += 1
            match_wake = wake_re.search(lines[index])
            if match_wake:
                end_time = int(match_wake.group(1))
            guards_totals[guard_id] += (end_time - start_time)
            guards_ranges[guard_id].append([start_time, end_time])
            index += 1

# find the guard who slept the most
max_sleep = 0
sleepiest_guard = ""
for guard, sleep in guards_totals.items():
    if sleep > max_sleep:
        max_sleep = sleep
        sleepiest_guard = guard

# find the sleepiest minute for this guard
most_sleep = 0
sleepiest_minute = 0
minutes = [0]*60
for span in guards_ranges[sleepiest_guard]:
    for i in range(span[0], span[1]):
        minutes[i] += 1
        if minutes[i] > most_sleep:
            most_sleep = minutes[i]
            sleepiest_minute = i

print("(Day 4, Part 1) sleepiest guard, most minutes: %d * %d = %d " % (int(sleepiest_guard), sleepiest_minute, int(sleepiest_guard) * sleepiest_minute))

# part 2: let's find the guard with the sleepiest minute instead
guards_minutes = {}
for guard, spans in guards_ranges.items():
    guards_minutes[guard] = [0]*60
    for span in spans:
        for i in range(span[0], span[1]):
            guards_minutes[guard][i] += 1

most_sleep = 0
sleepiest_minute = 0
sleepiest_guard = ""
for guard, minutes in guards_minutes.items():
    for i in range(0, 60):
        if minutes[i] > most_sleep:
            most_sleep = minutes[i]
            sleepiest_minute = i
            sleepiest_guard = guard

print("(Day 4, Part 2) sleepiest guard, sleepiest minute: %d * %d = %d " % (int(sleepiest_guard), sleepiest_minute, int(sleepiest_guard) * sleepiest_minute))
