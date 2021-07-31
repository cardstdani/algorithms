import random

def isSorted(n):
    for i in range(len(n) - 1):
        if n[i + 1] < n[i]:
            return False
    return True


def bubbleSort(n):
    while not isSorted(n):
        for i in range(len(n) - 1):
            if n[i + 1] < n[i]:
                n[i + 1], n[i] = n[i], n[i + 1]
    return n


array = random.sample(range(80), 10)
print(array)
print(bubbleSort(array))
print(isSorted(array))
