
data = []
with open("inputs/3.txt") as file:
    data = file.read().splitlines()


summed = 0

enabled = True
for line in data:
    for i in range(len(line)-6):

        if line[i:].startswith("do()"):
            enabled = True
        
        if line[i:].startswith("don't()"):
            enabled = False

        if enabled and line[i:].startswith("mul("):
            for j in range(i+4, len(line)):
                if line[j] == ")":
                    parsed = line[i+4:j].split(",")
                    if len(parsed) == 2 and parsed[0].isdigit() and parsed[1].isdigit():
                        print(parsed)
                        summed += int(parsed[0]) * int(parsed[1])
            
print(summed)