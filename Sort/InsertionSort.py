import random

def insertionSort(n):
    for i in range(1, len(n)):
        for a in range(i):
            if n[i] < n[a]:
                n[i], n[a] = n[a], n[i]
    return n

array = random.sample(range(80), 10)
print(array)
print(insertionSort(array))
