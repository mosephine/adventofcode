#! /usr/bin/python

import re
import math
from collections import deque, defaultdict

test_inputs = [
        "9 players; last marble is worth 25 points",
        "10 players; last marble is worth 1618 points",
        "13 players; last marble is worth 7999 points",
        "17 players; last marble is worth 1104 points",
        "21 players; last marble is worth 6111 points",
        "30 players; last marble is worth 5807 points"]

test_results = [
        32,
        8317,
        146373,
        2764,
        54718,
        37305]

real_inputs = [
        "448 players; last marble is worth 71628 points",
        "448 players; last marble is worth 7162800 points"]

input_re = re.compile("(\d+) players; last marble is worth (\d+) points")

# really elegant solution, but not mine
def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

def compute_score(line):
    re_groups = input_re.search(line)
    if not re_groups:
        return
    n_players = int(re_groups.group(1))
    n_marbles = int(re_groups.group(2))

    return play_game(n_players, n_marbles)

print("(Day 9, Part 1) max marble game score: " + str(compute_score(real_inputs[0])))
print("(Day 9, Part 2) max marble game score x 100: " + str(compute_score(real_inputs[1])))
