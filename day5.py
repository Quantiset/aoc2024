
data = []
with open("inputs/5.txt") as file:
    data = file.read().splitlines()

p1 = True
befores = {}
summed = 0
p2 = 0
for line in data:
    if line.replace(" ","") == "":
        p1 = False
        continue
    if p1:
        f, t = map(int, line.split("|"))
        if f in befores:
            befores[f].append(t)
        else:
            befores[f] = [t]
    
    else:
        arr = list(map(int, line.split(",")))

        is_for_p2 = False

        while True:
            is_corr = True
            for i in range(len(arr)-1,0,-1):
                if arr[i] in befores:
                    for j in range(i, -1, -1):
                        if arr[j] in befores[arr[i]]:
                            arr[i], arr[j] = arr[j], arr[i]
                            is_corr = False
                            is_for_p2 = True
                            break
                if not is_corr:
                    break
            if is_corr:
                break
        
        if is_for_p2:
            p2 += arr[ len(arr)//2 ]
        else:
            summed += arr[ len(arr)//2 ]
    


    
print(summed, p2)