from collections import deque
import heapq

data = {}
with open("inputs/16.txt") as file:
    data = file.read().splitlines()

rotations = {
    (0, 1): [(1, 0), (-1, 0)],
    (1, 0): [(0, -1), (0, 1)],
    (0, -1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, -1), (0, 1)]
}

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

start = None
end = None
for y, line in enumerate(data):
    for x, char in enumerate(line):

        if char == 'S':
            start = (x, y)
        elif char == 'E':
            end = (x, y)

def p1(prev_min = None):
    queue = []
    heapq.heappush(queue, (0, start, (1,0), [start]))
    visited = set()
    scores_at = {}

    mins = {}
    minned = 9999999

    while queue:
        # print(len(queue))
        cost, pos, direction, path = heapq.heappop(queue)

        if pos == end:
            if not cost in mins:
                mins[cost] = set(path)
            else:
                mins[cost] = mins[cost].union(set(path))
            minned = min(minned, cost)

        if not prev_min:
            if (pos, direction) in visited:
                continue
            visited.add((pos, direction))
        else:
            if cost > prev_min:
                continue
            if scores_at.get((pos, direction),99999999) < cost:
                # print("HID")
                continue
            scores_at[pos, direction] = cost

        next_pos = vadd(pos, direction)
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(data[0]) or next_pos[1] >= len(data):
            continue

        if (data[next_pos[1]][next_pos[0]] != '#'):
            heapq.heappush(queue, (cost + 1, next_pos, direction, path + [next_pos]))

        for new_dir in rotations[direction]:
            heapq.heappush(queue, (cost + 1000, pos, new_dir, path))

    return minned, len(mins[minned])



minned = p1()[0]
print(minned, p1(minned)[1])