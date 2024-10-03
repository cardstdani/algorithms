def maxCount(n):
    d={}
    m = 0
    element = 0
    for i in n:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > m:
            m = d[i]
            element = i
    return i


a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 2, 2]
print(maxCount(a1))
