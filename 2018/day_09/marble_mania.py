#! /usr/bin/python

import re
import math

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

def compute_score(line):
    re_groups = input_re.search(line)
    if not re_groups:
        return
    n_players = int(re_groups.group(1))
    n_marbles = int(re_groups.group(2))

    scores = [0] * n_players
    current_player = 0
    marble_index = 0
    marble_circle = [0]

    for i in range(1, n_marbles + 1):
        if i % 23 == 0: # special rules for these marbles
            print("[" + str(i) + "] " + str(marble_circle))
            new_index = 0
            if marble_index < 7:
                new_index = len(marble_circle) + (marble_index - 7)
            else:
                new_index = marble_index - 7
            scores[current_player] += marble_circle[new_index] + i
            marble_circle.pop(new_index)
            marble_index = new_index
        
        else:
            if i == 1:
                marble_index = 1
                marble_circle.append(i)
            else:
                marble_index = (marble_index + 2) % len(marble_circle)
                marble_circle.insert(marble_index, i)
        current_player = (current_player + 1) % n_players

    max_score = 0
    for score in scores:
        if score > max_score:
            max_score = score

    return max_score

compute_score(test_inputs[1])
#for i in range(0, len(test_inputs)):
    #value = compute_score(test_inputs[i])
    #print("Test %d compute = %d, actual = %d" % (i, value, test_results[i]))

print("(Day 9, Part 1) max marble game score: " + str(compute_score(real_inputs[0])))

# part 2, we need an equation to calculate scores
def equation_score(line):
    re_groups = input_re.search(line)
    if not re_groups:
        return
    n_players = int(re_groups.group(1))
    n_marbles = int(re_groups.group(2))

    scores = [0] * n_players
    current_winner = 0
    marble_count = 23
    iterations = 0
    while marble_count < n_marbles:
        current_winner = (current_winner + 23) % n_players
        to_subtract = (14 * (iterations + 1)) + math.factorial(iterations)
        scores[current_winner] += marble_count + (marble_count - to_subtract)
        marble_count += 23
        iterations += 1

    max_score = 0
    for score in scores:
        if score > max_score:
            max_score = score

    return max_score

for i in range(0, len(test_inputs)):
    value = equation_score(test_inputs[i])
    print("Test %d compute = %d, actual = %d" % (i, value, test_results[i]))

print("(Day 9, Part 1) max marble game score: " + str(equation_score(real_inputs[0])))
print("(Day 9, Part 2) max marble game score x 100: " + str(equation_score(real_inputs[1])))
