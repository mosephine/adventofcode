#! /usr/bin/python

import re

lines = [line.rstrip('\n') for line in open('test_input.txt')]

dep_re = re.compile("Step (\w+) must be finished before step (\w+) can begin.")

# create bi-directional dependency graph

def create_graph():
    steps = {}
    for line in lines:
        dep_values = dep_re.search(line)
        before = dep_values.group(1)
        after = dep_values.group(2)

        stepAfter = None
        if after in steps:
            stepAfter = steps[after]
        else:
            stepAfter = [set(), set()]
        stepBefore = None
        if before in steps:
            stepBefore = steps[before]
        else:
            stepBefore = [set(), set()]

        stepAfter[0].add(before)
        steps[after] = stepAfter
        stepBefore[1].add(after)
        steps[before] = stepBefore
    return steps

steps = create_graph()
# now that we have the full dependency graph, create the path
path = ""
next_steps = set()
total_steps = len(steps)
while total_steps > len(path):
    for value, step in steps.items():
        safe_to_add = True
        if step[0]:
            for item in step[0]:
                if item not in path:
                    safe_to_add = False;
        if safe_to_add:
            next_steps.add(value)
    if next_steps:
        next_steps_list = sorted(next_steps)
        to_add = next_steps_list[0]
        path += to_add
        steps.pop(to_add)
        next_steps.remove(to_add)
    

print("(Day 7, part 1) ordered steps: " + path)
    
# part 2, multi-workers
steps = create_graph()
total_steps = len(steps)
n_workers = 2
base_step_time = 0
workers = [[] for i in range(0, n_workers)]
ordinal_transform = 64

path = ""

# every time we add a new step to a worker queue, the last step in that queue is done
while total_steps > len(path):
    for value, step in steps.items():
        safe_to_add = True
        if step[0]:
            for item in step[0]:
                if item not in path:
                    safe_to_add = False;
        if safe_to_add:
            next_steps.add(value)
    if next_steps:
        next_steps_list = sorted(next_steps)
        to_add = next_steps_list[0]

        # now the tricky part, add to worker with shortest queue
        worker_id = 0
        for i in range(0, n_workers):
            if len(workers[i]) < len(workers[worker_id]):
                worker_id = i

        if len(workers[worker_id]) > 0:
            path += workers[worker_id][-1]
        steps.pop(to_add)
        next_steps.remove(to_add)
        
        workers[worker_id] += (ord(to_add) - ordinal_transform + base_step_time) * [to_add]


print("(Day 7, part 2) multi workers step order:" + path)
