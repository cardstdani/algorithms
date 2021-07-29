def gridPaths(x, y):
    if x == 1 or y == 1:
        return 1
    return gridPaths(x - 1, y) + gridPaths(x, y - 1)


print(gridPaths(2, 3))

def gridPathsMem(x, y, mem={}):
    id = str(min(x, y)) + "," + str(max(x, y))
    if (id) in mem:
        return mem[id]
    if x == 1 or y == 1:
        return 1
    mem[id] = gridPathsMem(x - 1, y, mem) + gridPathsMem(x, y - 1, mem)
    return mem[id]

print(gridPathsMem(18, 18))
