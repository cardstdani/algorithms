def recursiveLinearSearch(list, target, i=0):
  if list[i] == target:
    return i
  if list[len(list)-i-1] == target:
    return (len(list)-i-1)
  return recursiveLinearSearch(list, target, i+1)


myList = [0, 5, 8, 1, 763, 2, 9, 12]
print(myList)
print(recursiveLinearSearch(myList, 12))
