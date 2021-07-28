def stringWordReverse(s):
    return s.split()[::-1]
print(" ".join(stringWordReverse("Hello world")))

def stringReverse(s):
    r = ""
    for i in s:
        r = i + r
    return r
print(stringReverse("Hello world"))
