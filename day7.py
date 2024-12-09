
data = []
with open("inputs/7.txt") as file:
    data = file.read().splitlines()

def matches(test, vals, ops):

    if len(vals) == len(ops) + 1:
        ret = vals[0]
        for i, val in enumerate(vals[1:]):
            if ops[i] == "+":
                ret += val
            elif ops[i] == "*":
                ret *= val
            elif ops[i] == "|":
                ret = int(str(ret) + str(val))
        
        return ret == test
    
    for operation in "+*|":
        if matches(test, vals, ops + [operation]):
            return True
    return False
            

import time
before_your_code = time.time()

summed = 0
i = 0
for line in data:
    test, valss = line.split(": ")
    test = int(test)
    vals = list(map(int, valss.split(" ")))
    if matches(test, vals, []):
        summed += test

        
after_your_code = time.time()
print(after_your_code - before_your_code)

print(summed)

