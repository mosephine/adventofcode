#! /usr/bin/python

import re
import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

mask_re = re.compile("^mask = ([X10]+)$")
mem_re = re.compile("mem\\[(\d+)\\] = (\d+)$")

def mask_apply(mask, val):
    val_new = ""
    val_bin = '{0:b}'.format(int(val))
    val_bin = val_bin.rjust(36, '0')

    for i in range(0, len(mask)):
        index = len(mask) - i - 1
        if mask[index] == 'X':
            val_new = val_bin[index] + val_new
        else:
            val_new = mask[index] + val_new

    return int(val_new, 2)


memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

for line in lines:
    mask_match = mask_re.search(line)
    if mask_match:
        mask = mask_match.group(1)
        continue

    mem_match = mem_re.search(line)
    if mem_match:
        memory[mem_match.group(1)] = mask_apply(mask, mem_match.group(2))

total = 0
for key,val in memory.items():
    total += val

print("(Day 14, Part 1) sum of memory addresses: %d" % total)

# part 2

def mask_addr(mask, val):
    addrs = ['']
    val_bin = '{0:b}'.format(int(val)).zfill(36)

    for i in range(0, 36):
        if mask[i] == '0':
            for j in range(0, len(addrs)):
                addrs[j] = addrs[j] + val_bin[i]
        elif mask[i] == '1':
            for j in range(0, len(addrs)):
                addrs[j] = addrs[j] + '1'
        else:
            new_addrs = []
            for addr in addrs:
                new_addrs.append(addr + '0')
                new_addrs.append(addr + '1')
            addrs = new_addrs
    
    return addrs

memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

for line in lines:
    mask_match = mask_re.search(line)
    if mask_match:
        mask = mask_match.group(1)
        continue

    mem_match = mem_re.search(line)
    if mem_match:
        mems = mask_addr(mask, mem_match.group(1))
        for mem in mems:
            memory[int(mem, 2)] = int(mem_match.group(2))

total = 0
for key,val in memory.items():
    total += val

print("(Day 14, Part 2) sum of memory addresses: %d" % total)

