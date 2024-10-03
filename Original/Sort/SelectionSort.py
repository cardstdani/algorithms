import random

def selectionSort(list):
  sortedList = []
  t = 0
  while len(list) > 0:
    for i in range(len(list)):
      if list[i] < list[t]:
        t = i
    sortedList.append(list[t])
    list.pop(t)
    t = 0
  return sortedList

myList = random.sample(range(80), 5)
print(myList)
print(selectionSort(myList))
