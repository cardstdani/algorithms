import random

def mergeSort(list):
  if len(list) <= 1:
    return list
  
  mid = len(list)//2
  l = list[:mid]
  r = list[mid:]

  mergedList = mergeSort(l)
  mergedList.extend(mergeSort(r))
  mergedList.sort()
  return mergedList

myList = random.sample(range(80), 10)
print(mergeSort(myList))
