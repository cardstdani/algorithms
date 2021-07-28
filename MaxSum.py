def maxSum(list):
    if len(list) <= 1:
        return None
    
    s = []
    currentSum = 0
    for i in list:
        s.append(i)
        for a in list:
            if not a in s:
                if (a+i) > currentSum:
                    currentSum = a+i
    return currentSum

def recursiveMaxSum(list, currentSum=0):
    if len(list) <= 1:
        return currentSum
    for i in list:
        if (list[0]+i) > currentSum:
            currentSum = list[0]+i
    return recursiveMaxSum(list[1:], currentSum)
    
print(maxSum([1, 2, 3, 4, 5]))
