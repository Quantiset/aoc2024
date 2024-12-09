
data = []
with open("inputs/4.txt") as file:
    data = file.read().splitlines()

n = len(data[0])


def search(pos, dir, idx):
    if idx == 4:
        return True
    
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
        return False

    if data[ pos[1] ][ pos[0] ] == "XMAS"[idx]:
        return search( vadd(pos, dir), dir, idx + 1)
    
    return False

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def lived_mas(x, y):
    if data[y][x] != "A":
        return False
    
    if x <= 0 or x >= n - 1 or y <= 0 or y >= n - 1:
        return False
    
    s1 = set([ data[y-1][x-1], data[y+1][x+1] ])
    s2 = set([ data[y-1][x+1], data[y+1][x-1] ])

    if "S" in s1 and "M" in s1 and "S" in s2 and "M" in s2:
        return True
    
    return False

count = 0
count2 = 0
for y, line in enumerate(data):
    for x, c in enumerate(line):
        for dir in [ (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1) ]:
            if search( (x,y) , dir, 0):
                count += 1
        
        if lived_mas(x, y):
            count2 += 1

print(count, count2)