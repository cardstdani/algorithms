def bestSum(target, list):
    if target == 0:
        return []
    if target < 0:
        return None

    shortestPath = None
    for i in list:
        r = bestSum(target - i, list)
        if r != None:
            o = r[:]
            o.append(i)
            if shortestPath == None or len(o) < len(shortestPath):
                shortestPath = o
    return shortestPath

def bestSumMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortestPath = None
    for i in list:
        r = bestSumMem(target - i, list, mem)
        if r != None:
            o = r[:]
            o.append(i)
            if shortestPath == None or len(o) < len(shortestPath):
                shortestPath = o
    mem[target] = shortestPath
    return shortestPath

print(bestSum(8, [1, 4, 5]))
print(bestSumMem(100, [1, 2, 5, 25]))
