def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    
    d1 = {}
    d2 = {}
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
            
    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    return d1 == d2

print(anagram("dog", "god"))
