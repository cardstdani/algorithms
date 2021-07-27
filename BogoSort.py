import random

def isSorted(list):
  for i in range(1, len(list)):
    if list[i] < list[i-1]:
      return False
  return True

def bogoSort(list):
  while not isSorted(list):
    random.shuffle(list)
  return list

myList = random.sample(range(80), 5)
print(bogoSort(myList))
