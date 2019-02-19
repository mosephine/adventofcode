#! /usr/bin/python

from collections import deque

target = 894501
scores = [3, 7]

worker1 = 0
worker2 = 1

while len(scores) < (target + 10):
    worker1 = (worker1 + scores[worker1] + 1) % len(scores)
    worker2 = (worker2 + scores[worker2] + 1) % len(scores)

    combined_score = scores[worker1] + scores[worker2]
    for ch in str(combined_score):
        scores.append(int(ch))

print('(Day 14, Part 1) 10 scores after target # of recipes: ' + ''.join(map(str,(scores[target:target+10]))))

target_array = [int(x) for x in str(target)]
lookback = len(target_array) * -1
scores = [3, 7]

worker1 = 0
worker2 = 1

searching = True
while searching:
    worker1 = (worker1 + scores[worker1] + 1) % len(scores)
    worker2 = (worker2 + scores[worker2] + 1) % len(scores)

    combined_score = scores[worker1] + scores[worker2]
    for ch in str(combined_score):
        scores.append(int(ch))
        if scores[lookback:] == target_array:
            searching = False
            break

print('(Day 14, Part 2) number of recipes before target str reached: ' + str(len(scores[:lookback])))
