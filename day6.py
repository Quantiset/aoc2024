import sys

sys.setrecursionlimit(100000)

data = []
with open("inputs/6.txt") as file:
    data = file.read().splitlines()

next_dir = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

path = set()
places = set()

obstacles = set()

def adjacencies(pos):
    return [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]

def oob(pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data[0]) or pos[1] >= len(data)

def search(pos, dir, dirpath: set = set(), p2 = False):

    nextpos = vadd(pos, dir)
    while nextpos in obstacles:
        dir = next_dir[dir]
        nextpos = vadd(pos, dir)
    
    pos = nextpos
    if oob(pos):
        return False
    if (dir, pos) in dirpath:
        return True
    dirpath.add( (dir, pos) )

    if not p2:
        path.add(pos)

    return search(pos, dir, dirpath, p2)
    

def vadd(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

origin = (0, 0)

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            obstacles.add((x, y))
        
        if char == "^":
            origin = (x,y)

path.add(origin)
search(origin, (0, -1), set())


for y, line in enumerate(data):
    print(y)
    for x, char in enumerate(line):

        is_valid = False
        for adj in adjacencies((x, y)):
            if adj in path:
                is_valid = True
                break

        if char not in "#^" and is_valid:
            obstacles.add((x, y))
            if search(origin, (0, -1), set(), True):
                places.add((x, y))
            obstacles.remove((x, y))

print(len(path), len(places))