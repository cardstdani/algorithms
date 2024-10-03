def isRotation(n1, n2):
    index = 0
    for i in range(len(n1)):
        if n2[0] == n1[i]:
            index = i
            break
        if n2[0] == n1[len(n1) - i - 1]:
            index = (len(n1) - i - 1)
            break

    for i in range(len(n1)):
        if (i + index) >= len(n2):
            if not n2[i] == n1[(i + index) - len(n1)]:
                return False
        else:
            if not n2[i] == n1[i + index]:
                return False
    return True


a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
print(isRotation(a1, a2))
