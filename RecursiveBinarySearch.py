def recursiveBinarySearch(list, target, s, e):
  if (e-s) <= 1:
    if list[e] == target:
      return e
    elif list[s] == target:
      return s
    return None  
  mid = (e+s)//2
  if list[mid] == target:
    return mid
  elif list[mid] > target:
    return recursiveBinarySearch(list, target, s, mid)
  elif list[mid] < target:
    return recursiveBinarySearch(list, target, mid, e)

myList = list(range(0, 18, 2))
print(myList)
print(recursiveBinarySearch(myList, 4, 0, len(myList) - 1))
