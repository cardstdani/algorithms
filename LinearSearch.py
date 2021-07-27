def linearSearch(list, target):
  for i in range(len(list)):
    if target == list[i]:
      return i
  return None
