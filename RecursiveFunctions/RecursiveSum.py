def recursiveSum(list, i=0, r=0):
  if i >= len(list):
    return r
  else:
    return recursiveSum(list, i+1, r+list[i])

myList = random.sample(range(80), 5)
print(myList)
print(recursiveSum(myList))
