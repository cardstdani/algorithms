def uniqueCharacters(n):
    d = set()
    for i in n:
        if not i == " ":
            if not i in d:
                d.add(i)
            else:
                return False
    return True

s = "a b c d e f"
print(uniqueCharacters(s))
