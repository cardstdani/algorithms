def canConstruct(target, list):
    if len(target) == 0:
        return True

    for i in list:
        for a in range(len(i)):
            if not target[a] == i[a]:
                break
        newTarget = target[len(i):]
        if canConstruct(newTarget, list) == True:
            return True
    return False

def canConstructMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if len(target) == 0:
        return True

    for i in list:
        for a in range(len(i)):
            if not target[a] == i[a]:
                break
        newTarget = target[len(i):]
        if canConstructMem(newTarget, list, mem) == True:
            mem[target] = True
            return True
    mem[target] = False
    return mem[target]


print(canConstruct("abcdef", ["a", "b", "c", "d", "e", "f"]))
print(canConstructMem("abcdef", ["a", "b", "c", "d", "e", "f"]))

def canConstruct2(target, list):
    if len(target) == 0:
        return True

    for i in list:
        if target.find(i) == 0:
            newTarget = target[len(i):]
            if canConstruct(newTarget, list) == True:
                return True
    return False

def canConstructMem2(target, list, mem={}):
    if target in mem:
        return mem[target]
    if len(target) == 0:
        return True

    for i in list:
        if target.find(i) == 0:
            newTarget = target[len(i):]
            if canConstructMem(newTarget, list, mem) == True:
                mem[target] = True
                return True
    mem[target] = False
    return mem[target]


print(canConstruct2("abcdef", ["a", "b", "c", "d", "e", "f"]))
print(canConstructMem2("abcdef", ["a", "b", "c", "d", "e", "f"]))
