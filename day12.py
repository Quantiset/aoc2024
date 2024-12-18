
data = []
connections = {}
marked = set()

from collections import deque

with open("inputs/12.txt") as file:
    data = file.read().splitlines()

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1])

def get_type_at(pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data[0]) or pos[1] >= len(data):
        return None
    return data[pos[1]][pos[0]]

def info(pos, v_type):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data[0]) or pos[1] >= len(data):
        return (0, 0, 0)
    if data[pos[1]][pos[0]] != v_type:
        return (0, 0, 0)
    if pos in marked:
        return (0, 0, 0)

    area = 0
    per = 0
    edges = 0
    nonconnectionsarray = []
    queue = deque([pos])
    local_marked = set()

    while queue:
        pos = queue.popleft()

        if pos in marked:
            continue

        marked.add(pos)
        local_marked.add(pos)

        area += 1
        nonconnectionsarray = []
        othernonconnectionsarray = []

        for edge in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            c_pos = vadd(pos, edge)
            if (v_type, c_pos) in connections:
                for a in connections[v_type, c_pos]:
                    othernonconnectionsarray.append(a)

        for edge in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            c_pos = vadd(pos, edge)
            if get_type_at(c_pos) != v_type:
                per += 1
                if edge not in othernonconnectionsarray:
                    edges += 1
                nonconnectionsarray.append(edge)
            elif c_pos not in marked and c_pos not in queue:
                queue.append(c_pos)

        connections[v_type, pos] = nonconnectionsarray

    return (area, per, edges)

values = []
for y, line in enumerate(data):
    for x, val in enumerate(line):
        ri = info((x,y), val)
        # if ri[:3] != (0,0,0):
        #     print(val, (x,y), ri[:3])
        values.append(ri)

p1 = 0
p2 = 0
for val in values:
    p1 += val[0] * val[1]
    p2 += val[0] * val[2]

print(p1, p2)
