
data = []
with open("inputs/11.txt") as file:
    data = file.read().splitlines()

line = list(map(int, data[0].split(" ")))

cache = {}
def get_len(val, iters):
    # print(val, iters)
    if iters == 0:
        return 1
    
    # print(val, iters)
    if (val, iters) in cache:
        return cache[val, iters]

    query = []
    sval = str(val)
    if val == 0:
        query.append(1)
    elif len(sval) % 2 == 0:
        left = sval[:len(sval)//2]
        right = sval[len(sval)//2:]
        query.append( int(left) )
        query.append( int(right) )
    else:
        query.append(val * 2024)
    ret = 0
    for val in query:
        ret += get_len(val, iters-1)
    cache[(int(sval), iters)] = ret
    return ret


summed = 0
for val in line:
    summed += get_len(val, 75)

# print(cache)
print(summed)