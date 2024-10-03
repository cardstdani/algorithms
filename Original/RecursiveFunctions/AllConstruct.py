def allConstruct(target, list):
    if len(target) == 0:
        return [[]]

    out = []
    for i in list:
        if target.find(i) == 0:
            p = allConstruct(target[len(i):], list)
            for a in p:
                a.insert(0, i)
            out.extend(p)
    return out


def allConstructMem(target, list, mem={}):
    if target in mem:
        return mem[target]
    if len(target) == 0:
        return [[]]

    out = []
    for i in list:
        if target.find(i) == 0:
            p = allConstruct(target[len(i):], list)
            for a in p:
                a.insert(0, i)
            out.extend(p)
    mem[target] = out
    return out

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstructMem("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
