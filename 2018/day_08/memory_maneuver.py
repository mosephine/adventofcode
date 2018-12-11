#! /usr/bin/python

lines = [line.rstrip('\n') for line in open('input.txt')]
tokens = lines[0].split()

# part 1, sum of metadata
root_node = [[], []] 
tokens_index = 0
metadata_sum = 0

def read_header():
    global tokens_index
    return int(tokens[tokens_index]), int(tokens[tokens_index + 1])

def add_child(node):
    global tokens_index
    n_children, n_metadata = read_header()
    tokens_index += 2
    for i in range(0, n_children):
        new_node = [[], []]
        add_child(new_node)
        node[0].append(new_node)
    for i in range(0, n_metadata):
        add_metadata(node)
        tokens_index += 1


def add_metadata(node):
    global tokens_index, metadata_sum
    metadata_sum += int(tokens[tokens_index])
    node[1].append(int(tokens[tokens_index]))

add_child(root_node)
print("(Day 8, Part 1) sum of metadata: " + str(metadata_sum))

# part 2, value of root node
def node_value(node, value):
    if node[0]:
        for child in node[1]:
            if child <= len(node[0]):
                value = node_value(node[0][child - 1], value)
    else:
        for metadata in node[1]:
            value += metadata
    return value

print("(Day 8, Part 2) value of root node: " + str(node_value(root_node, 0)))
