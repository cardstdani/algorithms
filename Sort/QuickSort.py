import random

def quickSort(list):
  if len(list) <= 1:
    return list
  pivot = 0
  l = []
  r = []
  for i in range(1, len(list)):
    if list[i] <= list[pivot]:
      l.append(list[i])
    else:
      r.append(list[i])
  return quickSort(l) + [list[pivot]] + quickSort(r)

myList = random.sample(range(80), 5)
print(myList)
print(quickSort(myList))
