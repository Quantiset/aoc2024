
with open("inputs/15.txt") as file:
    data = file.read().splitlines()

chart = []
directions = ""
pos = (0,0)

dir_to_vec = {
    "^": (0,-1),
    "v": (0,1),
    "<": (-1,0),
    ">": (1,0)
}

is_dir = False
for y, line in enumerate(data):

    if is_dir:
        directions += line
        continue

    if line.strip() == "":
        is_dir = True
        continue

    chart.append([])
    for x, char in enumerate(line):
        if char == "O":
            chart[y].append("[")
            chart[y].append("]")
            continue
        if char == "@":
            pos = (x*2,y)
            char = "."
        chart[y].append(char)
        chart[y].append(char)

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1])

def push(dir):
    global pos
    new_pos = vadd(pos, dir)
    if chart[new_pos[1]][new_pos[0]] == "#":
        return
    if chart[new_pos[1]][new_pos[0]] == ".":
        pos = new_pos
        return

    # O ahead
    to_move = []
    end_ptr = new_pos
    this_layer = set()
    layers = []

    def add_to_layer(layer: set, tpos):
        layer.add(tpos)
        to_move.append(tpos)
        if chart[tpos[1]][tpos[0]] == "[":
            layer.add(vadd(tpos, (1,0)))
            to_move.append(vadd(tpos, (0,1)))
        if chart[tpos[1]][tpos[0]] == "]":
            layer.add(vadd(tpos, (-1,0)))
            to_move.append(vadd(tpos, (0,-1)))

    if not dir in [(0,1), (0,-1)]:
        while chart[end_ptr[1]][end_ptr[0]] in "[]":
            to_move.append(end_ptr)
            end_ptr = vadd(end_ptr, dir)
        if chart[end_ptr[1]][end_ptr[0]] == "#":
            return
        
        
        to_move = to_move[::-1]
        for move in to_move:
            new_vec = vadd(move, dir)
            chart[new_vec[1]][new_vec[0]] = chart[move[1]][move[0]]
        chart[new_pos[1]][new_pos[0]] = "."
        pos = new_pos

    else:
        
        add_to_layer(this_layer, new_pos)

        is_valid = [True]

        def is_has_space(layer):
            if len(layer) == 0:
                return False
            for tpos in layer:
                above = vadd(tpos, dir)
                if chart[above[1]][above[0]] in "#":
                    is_valid[0] = False
                    return False
            return True
        
        layers.append(this_layer)
        while is_has_space(this_layer):
            next_layer = set()
            for tpos in this_layer:
                query_pos = vadd(tpos, dir)
                if chart[query_pos[1]][query_pos[0]] in "[]":
                    add_to_layer(next_layer, query_pos)
            this_layer = next_layer
            layers.append(this_layer)
        
        if not is_valid[0]:
            return

        layers = layers[::-1]
        for layer in layers:
            for pos in layer:
                above = vadd(pos, dir)
                chart[above[1]][above[0]] = chart[pos[1]][pos[0]]
                chart[pos[1]][pos[0]] = "."
        pos = new_pos

for direction in directions:
    push(dir_to_vec[direction])
    
    # print(direction, pos)
    # for line in chart:
    #     print("".join(line))

summed = 0
for y, line in enumerate(chart):
    for x, char in enumerate(line):
        if char == "[":
            summed += 100 * y + x

# push((-1,0))

# push((0,1))
# push((0,1))


# push((-1,0))
# push((-1,0))
# push((-1,0))

# push((0,-1))

# print state
for line in chart:
    print("".join(line))


print(summed, pos)