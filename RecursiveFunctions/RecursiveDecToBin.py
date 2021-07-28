def toBinary(n, r=""):
    if n < 1:
        return r
    return toBinary(n//2, str(n%2) + str(r))
print(toBinary(852))
