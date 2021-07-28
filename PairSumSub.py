def pairSumSub(list, n):
    if len(list) <= 1:
        return None
        
    s = []
    output = []
    
    for i in list:
        t = abs(n-i)
        
        if t in s:
            output.append([i, t])
        else:
            s.append(i)
    return output
    
print(pairSum([3, 7, 15, 13, 7, 1, 2, 2], 6))
