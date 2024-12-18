
data = []
with open("inputs/10.txt") as file:
    data = file.read().splitlines()

def score(pos, curr, trailheads, p2):

    if pos[0] < 0 or pos[0] >= len(data[0]) or pos[1] < 0 or pos[1] >= len(data):
        return 0
    
    if data[pos[1]][pos[0]] != str(curr):
        return 0

    if curr == 9:
        if data[pos[1]][pos[0]] == "9" and (not pos in trailheads if not p2 else True):
            trailheads.add(pos)
            return 1
        return 0
    
    ret = 0
    ret += score((pos[0], pos[1] + 1), curr + 1, trailheads, p2)
    ret += score((pos[0], pos[1] - 1), curr + 1, trailheads, p2)
    ret += score((pos[0] + 1, pos[1]), curr + 1, trailheads, p2)
    ret += score((pos[0] - 1, pos[1]), curr + 1, trailheads, p2)
    return ret
    

summed = 0
p2 = 0
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "0":
            summed += score((x, y), 0, set(), False)
            p2 += score((x, y), 0, set(), True)
print(summed, p2)