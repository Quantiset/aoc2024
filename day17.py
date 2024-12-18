
data = {}
with open("inputs/17.txt") as file:
    data = file.read().splitlines()

a, b, c = 0,0,0

a = int(data[0].removeprefix("Register A: "))
b = int(data[1].removeprefix("Register B: "))
c = int(data[2].removeprefix("Register C: "))

sops = data[4].removeprefix("Program: ")
ops = list(map(int, sops.split(",")))

def get_output(a,b,c):

    def get_val(val):
        if val <= 3:
            return val
        if val == 4:
            return a
        if val == 5:
            return b
        if val == 6:
            return c

    out = ""
    i = 0
    while i < len(ops):
        opcode = ops[i]
        lit = ops[i+1]
        combo = get_val(lit)

        if opcode == 0:
            a = int(a / (2**combo))
        elif opcode == 1:
            b = b ^ lit
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a != 0:
                i = lit
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            out += str(combo % 8)+","
        elif opcode == 6:
            b = int(a / (2**combo))
        elif opcode == 7:
            c = int(a / (2**combo))
        
        i += 2
    return list(map(int,out[:-1].split(",")))

# print(get_output(a,b,c)) 

cost = (99999999999, 0)

13397658000000 + 139765800000*1354 + 139765800*4 + 2097152*188

# print(13397658000000 + 139765800000*1354 + 139765800*4 + 2097152*188 + 738442)
# for i in range(49):
#     q_pos = get_output((13397658000000 + 139765800000*1354 + 139765800*4 + 2097152*188 + 738442)//8,b,c)
#     if list(map(int,q_pos.split(","))) == ops:
#         print("QUERY HIT<<")
#         exit(0)

#     t_cost = 0
#     iq = list(map(int, q_pos.split(",")))
#     # check if last 8 numbers are the same for iq and ops
#     if iq[7:] == ops[7:] and len(iq) == len(ops):
#         cost = (t_cost, i)
#         print("Q: ", iq, i)
#         break
#     if iq[:7] == [2,4,1,1,7,5,4]:
#         print("Q: ", iq, i)
#         # break
    
#     print(iq)
# # print(l, r)

# -7: 1507748

BASE = 1507748*8*8*8*8*8*8*8*8*8+8*8*8*8*8*8*8*8+8*8*8*8*24320+10794

print(get_output(BASE, b, c))
# print(get_output(BASE+8*8*8*8*8*8*8*8*8, b, c))
print(ops)

print(BASE)

# for i in range(1000000):
#     i -= 1000
#     ret = get_output(BASE+i, b, c)
#     if ret == ops:
#         print("FOUND", i)
#         break
#     # print(ret)
#     if i % 8*8 == 8:
#         print(ret[-10:])


# print(get_output(5099*8*8*8*8-1, b, c))