#! /usr/bin/python


# to find the two entires summing to 2020, insert entry into a hash if (2020 - entry) doesn't already exist
entries = [int(line.rstrip('\n')) for line in open('data.in')]
entry_set = set()
for entry in entries:
    inverse = 2020 - entry
    if inverse in entry_set:
        print("(Day 1, Part 1) %d + %d = 2020, product is %d" % (entry, inverse, entry * inverse))
        break
    else:
        entry_set.add(entry)


# finding 3 entries that add to 2020 is harder, hmm...
end = False
for i in range(0,len(entries)):
    for j in range(1, len(entries)):
        for k in range(2, len(entries)):
            val = entries[i] + entries[j] + entries[k]
            if val == 2020:
                print("(Day 1, Part 2) %d + %d + %d = 2020, product is %d" % (entries[i], entries[j], entries[k], entries[i] * entries[j] * entries[k]))
                end = True
                break

        if end:
            break
    if end:
        break

