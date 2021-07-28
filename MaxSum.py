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
        
    
print(maxSum([1, 2, 3, 4, 5]))
