def advancedPairSum(target, list):
    if target == 0:
        return []
    if target < 0:
        return None

    for i in list:
        r = advancedPairSum(target - i, list)
        if r != None:
            o = r[:]
            o.append(i)
            return o
    return None

def advancedPairSumMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for i in list:
        r = advancedPairSumMem(target - i, list, mem)
        if r != None:
            o = r[:]
            o.append(i)
            mem[target] = o
            return mem[target]
    mem[target] = None
    return mem[target]

print(advancedPairSum(7, [2, 3]))
print(advancedPairSumMem(7, [2, 3]))
