import numpy as np
import math

machines = []
with open("inputs/13.txt") as file:
    data = file.read().splitlines()

va, vb, vt = None, None, None
for line in data + [""]:  
    line = line.strip()
    if not line:
        if va and vb and vt:
            machines.append((va, vb, vt))
        va, vb, vt = None, None, None
    elif line.startswith("Button A:"):
        va = tuple(map(int, line.replace("Button A: X+", "").replace("Y+", "").split(", ")))
    elif line.startswith("Button B:"):
        vb = tuple(map(int, line.replace("Button B: X+", "").replace("Y+", "").split(", ")))
    elif line.startswith("Prize:"):
        vt = tuple(map(int, line.replace("Prize: X=", "").replace("Y=", "").split(", ")))


def solve(a,b):
    print(a,b)
    det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    x = (b[0]*a[1][1] - b[1]*a[0][1]) / det
    y = (a[0][0]*b[1] - a[1][0]*b[0]) / det
    return x, y

total_cost = 0
for va, vb, vt in machines:
    a = np.array([[va[0], vb[0]], [va[1], vb[1]]])
    b = np.array( (10000000000000 + vt[0], 10000000000000 + vt[1] ) )

    x = solve(a, b)
    if int(x[0]) != x[0] or int(x[1]) != x[1]:
        continue
    total_cost += x[0] * 3 + x[1]

print(total_cost)

