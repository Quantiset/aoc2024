data = {}
with open("inputs/18.txt") as file:
    data = file.read().splitlines()

start = (0,0)
end = (70,70)
UPTO = 1024

blocks = set()

import heapq

def bfs(start, end):
    queue = []
    heapq.heappush(queue, (0, start, []))
    visited = set()

    while queue:
        dist, pos, path = heapq.heappop(queue)

        if pos == end:
            return dist, path

        if pos in visited:
            continue

        visited.add(pos)

        for edge in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0]+edge[0], pos[1]+edge[1])
            if new_pos in blocks:
                continue
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > end[0] or new_pos[1] > end[1]:
                continue
            heapq.heappush(queue, (dist+1, new_pos, path+[new_pos]))
    return -1


for i, line in enumerate(data):
    if i == UPTO:
        break
    pos = tuple(map(int, line.split(",")))
    blocks.add(pos)

costa, path = bfs(start, end)

print(costa)

for i, line in enumerate(data):
    if i < UPTO:
        continue
    pos = tuple(map(int, line.split(",")))
    blocks.add(pos)

    if pos in path:
        pt = bfs(start, end)
        if pt == -1:
            print(pos)
            break
        costa, path = pt
