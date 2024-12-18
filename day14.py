
with open("inputs/14.txt") as file:
    data = file.read().splitlines()

DIM = (101, 103)
STEPS = 100

robots = []

for line in data:
    pos, vel = line.split(" ")
    pos = tuple(map(int, pos.removeprefix("p=").split(",")))
    vel = tuple(map(int, vel.removeprefix("v=").split(",")))
    robots.append((pos, vel))

after_robots = []
for robot in robots:
    pos, vel = robot
    after_robots.append(( (pos[0] + STEPS *  vel[0]) % DIM[0], (pos[1] + STEPS * vel[1]) % DIM[1] ))

def get_image(iterations):
    image = [["." for _ in range(DIM[0])] for _ in range(DIM[1])]
    for robot in robots:
        pos, vel = robot
        image[ (pos[1] + iterations* vel[1]) % DIM[1] ][ (pos[0] + iterations*vel[0]) % DIM[0] ] = "#"
    return image

import math
def centrality_score(iterations):
    ret = 0
    for robot in robots:
        pos, vel = robot
        dist = math.sqrt(( ((pos[1] + iterations* vel[1]) % DIM[1]) - DIM[1]/2 )**2 + ( ((pos[0] + iterations*vel[0]) % DIM[0]) - DIM[0]/2 ) ** 2)
        ret += 1/dist
    return ret

def get_quadrant(pos):
    if pos[0] == DIM[0] // 2:
        return -1
    if pos[1] == DIM[1] // 2:
        return -1
    if pos[0] < DIM[0] / 2 and pos[1] < DIM[1] / 2:
        return 0
    elif pos[0] > DIM[0] / 2 and pos[1] < DIM[1] / 2:
        return 1
    elif pos[0] < DIM[0] / 2 and pos[1] > DIM[1] / 2:
        return 2
    elif pos[0] > DIM[0] / 2 and pos[1] > DIM[1] / 2:
        return 3
    return -1

quadrants = [0, 0, 0, 0, 0]
for robot in after_robots:
    print(robot, get_quadrant(robot))
    quadrants[get_quadrant(robot)] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

min_centrality = (0,0)
for i in range(10000):
    # print(i, centrality_score(i))
    if min_centrality[1] < centrality_score(i):
        min_centrality = (i, centrality_score(i))
print(
    "\n".join(
        ["".join(row) for row in get_image(min_centrality[0])]
    )
)
print(min_centrality)