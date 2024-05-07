l1 = [550,600,700,650,700,500]
l2 = [7,7,7,7,7]
l3 = [0,5,3,4,1,2]
l4 = [6,4,5,6,0,0,8]

def g(l, w):
    m = max(l)
    tmp = sum(l[:w])    
    m_count = sum(1 for i in l[:w] if i==m)    
    out = [tmp if m_count > 0 else 0,0]
    for i in range(len(l)-w):
        m_count-=1 if l[i]==m else 0    
        m_count+=1 if l[i+w]==m else 0
        tmp-=l[i]
        tmp+=l[i+w] if (i+w)<len(l) else 0
        if tmp >= out[0] and m_count>0:
            out = [tmp, i+1]        
    return [out[0], out[1]+1]

print(g(l1,2))
print(g(l2,3))
print(g(l3,2))
print(g(l4,2))