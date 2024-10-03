import random

def quickSort(list):
  if len(list) <= 1:
    return list
  pivot = len(list)//2
  l = []
  r = []
  for i in range(len(list)):
    if not i == pivot:
      if list[i] <= list[pivot]:
        l.append(list[i])
      else:
        r.append(list[i])
  return quickSort(l) + [list[pivot]] + quickSort(r)

myList = random.sample(range(80), 5)
print(myList)
print(quickSort(myList))
