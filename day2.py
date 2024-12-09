
data = []
with open("inputs/2.txt") as file:
    data = file.read().splitlines()

nums = 0
for line in data:
    
    allowed = False
    arr = list(map(int, line.split()))

    for k in range(len(arr)):
        t_arr = arr.copy()
        t_arr.pop(k)
        for sign in [-1, 1]:
            s_t = False
            for i in range(len(t_arr)-1):
                if sign * (t_arr[i+1] - t_arr[i]) >= 4 or sign * (t_arr[i+1] - t_arr[i]) <= 0:
                    s_t = True
                    break
            if s_t:
                continue
            allowed = True
        
        if allowed:
            nums += 1
            break

print(nums)
            