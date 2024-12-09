
data = []
with open("inputs/8.txt") as file:
    data = file.read().splitlines()

f_set = set()
frequencies = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            f_set.add( (x,y) )
            if not char in frequencies:
                frequencies[char] = [(x,y)]
            else:
                frequencies[char].append((x,y))

import itertools

def vadd(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def vneg(v):
    return (-v[0], -v[1])

def is_valid_node(v):
    return v[0] >= 0 and v[1] >= 0 and v[0] < len(data[0]) and v[1] < len(data)

antinodes = set()
for char in frequencies:
    for pos_a, pos_b in itertools.combinations(frequencies[char], 2):

        temp = set()
        vel = vadd(pos_a, vneg(pos_b))

        tmp_pos = pos_a
        for i in range(1000):
            temp.add(tmp_pos)
            tmp_pos = vadd(tmp_pos, vel)
        
        vel = vadd(pos_b, vneg(pos_a))
        tmp_pos = pos_a
        for i in range(1000):
            temp.add(tmp_pos)
            tmp_pos = vadd(tmp_pos, vel)

        antinodes = antinodes.union(temp)


pared_set = set()
count = 0
for val in antinodes:
    if is_valid_node(val):
        pared_set.add(val)

print(len(pared_set))