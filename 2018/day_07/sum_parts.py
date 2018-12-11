#! /usr/bin/python

import re
import operator

lines = [line.rstrip('\n') for line in open('input.txt')]

dep_re = re.compile("Step (\w+) must be finished before step (\w+) can begin.")

# create bi-directional dependency graph

def create_graph():
    steps = {}
    for line in lines:
        dep_values = dep_re.search(line)
        before = dep_values.group(1)
        after = dep_values.group(2)

        stepAfter = steps[after] if after in steps else [set(), set()]
        stepBefore = steps[before] if before in steps else [set(), set()]

        stepAfter[0].add(before)
        steps[after] = stepAfter
        stepBefore[1].add(after)
        steps[before] = stepBefore
    return steps

steps = create_graph()

# part 1, now that we have the full dependency graph, create the path
path = ""
next_steps = set()
while len(steps) > len(path):
    for value, step in steps.items():
        if value in path:
            continue
        safe_to_add = True
        if step[0]:
            for item in step[0]:
                if item not in path:
                    safe_to_add = False
        if safe_to_add:
            next_steps.add(value)
    if next_steps:
        to_add = sorted(next_steps)[0]
        path += to_add
        next_steps.remove(to_add)
    

print("(Day 7, part 1) ordered steps: " + path)
    
# part 2, multi-workers
n_workers = 5
base_time = 60
transform = -64

workers = [[] for i in range(0, n_workers)]
end_times = {}
next_steps = set()

# need the total time, not the path
while len(steps) > len(end_times):
    for value, step in steps.items():
        if value in end_times:
            continue
        safe_to_add = True
        if step[0]:
            for item in step[0]:
                if item not in end_times:
                    safe_to_add = False;
        if safe_to_add:
            next_steps.add(value)

    while next_steps:
        current_step = sorted(next_steps)[0]
        next_steps.discard(current_step)
        
        start_time = 0
        for item in steps[current_step][0]:
            if start_time < end_times[item]:
                start_time = end_times[item]
            
        shortest_wait = 0
        next_worker = 0
        shortest_queue = len(workers[0])
        for i in range(0, n_workers):
            if len(workers[i]) <= start_time:
                next_worker = i
                shortest_wait = start_time - len(workers[i])
                break
            else:
                if shortest_queue > len(workers[i]):
                    shortest_queue = len(workers[i])
                    next_worker = i
        
        if shortest_wait > 0:
            workers[next_worker] += [0] * shortest_wait
        
        work_time = ord(current_step) + base_time + transform
        workers[next_worker] += [current_step] * work_time
        end_times[current_step] = len(workers[next_worker])

sorted_by_time = sorted(end_times.items(), key=operator.itemgetter(1))

print("(Day 7, part 2) multi workers total time: " + str(sorted_by_time[-1][1]))

