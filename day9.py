
data = []
with open("inputs/9.txt") as file:
    data = file.read().splitlines()

inp = list(map(int, list(data[0])))

mem = []

for i, am in enumerate(inp):
    if i % 2 == 0:
        for j in range(am):
            mem.append(i // 2)
    else:
        for j in range(am):
            mem.append(-1)

def has(mem):
    summed = 0
    for i, val in enumerate(mem):
        if val == -1:
            val = 0
        summed += val * i
    return summed

def p1(mem):
    j = len(mem) - 1
    for i in range(len(mem)):
        val = mem[i]
        if i == j:
            break
        if val == -1:
            mem[i] = mem[j]
            mem[j] = 0
            j -= 1
            while mem[j] == -1:
                mem[j] = 0
                j -= 1
    return has(mem)

def p2(mem):
    next_j = len(mem) - 1
    for j in range(len(mem)-1, 0, -1):
        mval = mem[j]
        if mval == -1:
            continue

        if j > next_j:
            continue

        mlen = 0
        while mem[j-mlen] == mval:
            mlen += 1
        next_j = j - mlen
            
        next_i = 0
        for i in range(j):
            
            val = mem[i]
            if val != -1:
                continue

            if i < next_i:
                continue
            
            empty = 0
            while mem[i+empty] == -1:
                empty += 1
            next_i = i + empty

            if empty >= mlen:

                # print(mem)
                
                for k in range(mlen):
                    mem[i+k] = mval
                    mem[j-k] = -1
                
                # print(empty, mlen, mval, mem)

                break
    return has(mem)



# print(mem)

print(p1(mem.copy()), p2(mem.copy()))