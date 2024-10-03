def countConstruct(target, list):
    if len(target) == 0:
        return 1

    count = 0
    for i in list:
        if target.find(i) == 0:
            newTarget = target[len(i):]
            count += countConstruct(newTarget, list)
    return count


def countConstructMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if len(target) == 0:
        return 1

    count = 0
    for i in list:
        if target.find(i) == 0:
            newTarget = target[len(i):]
            count += countConstructMem(newTarget, list, mem)
    mem[target] = count
    return count


print(countConstruct("abcdef", ["a", "b", "c", "d", "e", "f"]))
print(countConstructMem("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
