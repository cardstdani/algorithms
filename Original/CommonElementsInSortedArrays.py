def commonElements(n1, n2):
    out = []
    if len(n2) < len(n1):
        n1, n2 = n2, n1
    for i in range(len(n1)):
        for a in range(len(n2)):
            if n1[0] == n2[a]:
                out.append(n1[0])
                n1.pop(0)
                n2.pop(0)
                break
            if n1[0] < n2[a]:
                n1.pop(0)
                break
            else:
                n2.pop(0)
                break
    return out


a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [1, 3, 6, 8, 11, 12, 13, 14, 16, 20]
print(commonElements(a1, a2))
