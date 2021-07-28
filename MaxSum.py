def maxSum(list):
    if len(list) <= 1:
        return None
    
    s = []
    sums = []
    for i in list:
        s.append(i)
        for a in list:
            if not a in s:
                sums.append(a+i)
    return max(sums)
        
    
print(maxSum([1, 2, 3, 4, 5]))
