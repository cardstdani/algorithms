def binarySearch(list, target):
  start = 0
  end = len(list)
  while start < end:
    mid = (end - start)//2
    if list[mid] == target:
      return mid
    elif (end-start) <= 1:
      return None
    elif list[mid] > target:
      end = end//2
    elif list[mid] < target:
      start = end//2    
  return None

print(binarySearch([0, 1, 2, 3, 4, 5, 6], 2))
