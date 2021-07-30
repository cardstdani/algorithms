def canSum(target, list):
    arr = [0]*target
    arr[0] = 1
    for a in range(target):
        if arr[a] == 1:
            for i in list:
                if (a+i) == target:
                    return True
                if (a+i) < target:
                    arr[a+i] = 1
    return False

print(canSum(7, [0]))
print(canSum(7, [2, 3]))
print(canSum(300, [7, 14]))
