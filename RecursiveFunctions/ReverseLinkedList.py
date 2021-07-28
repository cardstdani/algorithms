class node():
  def __init__(self, d, n):
    self.data = d
    self.next = n

  def __str__(self):
    return(str(self.data) + " " + str(self.next))

def insert(d, index=None):
  temp = head
  if index == None:
    while not temp.next == None:
      temp = temp.next
    temp.next = node(d, None)
  else:
    for i in range(index):
      temp = temp.next
    temp2 = temp.next
    temp.next = node(d, temp2)
  return None

def printLinkedList():
  temp = head
  print(str(temp.data) + " " + str(temp.next))
  return None

def delete(index, head):
  temp = head
  if index == 0:
        head = head.next
  else:
    for i in range(index - 1):
      if (temp.next != None):
        temp = temp.next
      else:
        temp = None
        return
            
  temp2 = temp.next
  if temp2 == None:
    temp = None
    return
  temp.next = temp2.next  

def set(index, data):
  temp = head
  
  for i in range(index):
    if (temp.next != None):
      temp = temp.next;
    else:
      temp.data = data
      return        
  temp.data = data 

def reverse():
  global head
  temp2 = head
  temp1 = None
  temp3 = None
  
  while not (temp2 == None):
    temp3 = temp2.next
    temp2.next = temp1
    temp1 = temp2
    temp2 = temp3
  head = temp1

def recursiveReverse(n, prev=None):
  if n == None:
    return prev
  temp = n.next
  n.next = prev
  return recursiveReverse(temp, n)

head = node(1, None)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6, 4)
delete(1, head)
set(4, 7)
printLinkedList()
head = recursiveReverse(head)
printLinkedList()
