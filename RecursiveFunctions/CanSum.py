def canSum(target, list):
    if target == 0:
        return True
    if target < 0:
        return False

    for i in list:
        if canSumMem(target - i, list) == True:
            return True
    return False

def canSumMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in list:
        mem[target - i] = canSumMem(target - i, list, mem)
        if mem[target - i] == True:
            return True
    mem[target] = False
    return mem[target]

print(canSum(3000, [7, 14]))
print(canSumMem(300, [7, 14]))
