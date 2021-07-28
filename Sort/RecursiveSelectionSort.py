import random

def recursiveSelectionSort(list, sorted=[]):
  if len(list) > 0:
    min = 0
    for i in range(len(list)):
      if list[i] < list[min]:
        min = i
    sorted.append(list[min])
    list.pop(min)
    return recursiveSelectionSort(list, sorted)
  else:
    return sorted

myList = random.sample(range(80), 5)
print(myList)
print(recursiveSelectionSort(myList))
