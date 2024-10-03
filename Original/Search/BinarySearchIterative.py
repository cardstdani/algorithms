def binarySearch(list, target):
  start = 0
  mid = 0
  end = len(list)
  while start < end:
    mid = (end + start)//2
    if list[mid] == target:
      return mid
    elif (end-start) <= 1:
      return None
    elif list[mid] > target:
      end = mid
    elif list[mid] < target:
      start = mid
  return None

print(binarySearch([0, 1, 2, 3, 4, 5, 6], 4))
