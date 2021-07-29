def firstUniqueCharacters(n):
    d = {}
    for i in n:
        if not i == " ":
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
    for i in d:
        if d[i] == 1:
            return i

s = "a b c d e f a"
print(firstUniqueCharacters(s))
