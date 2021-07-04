import matplotlib.pyplot as plt
from timeit import default_timer as timer

def function1(n):
  r = 0
  for i in n:
    r += i
  return r

def function2(n):
  r = 0
  for i in n:
    for a in range(len(n)):
      r+=1
    r += i
  return r

x = []
y = []

for i in range(0, 1000, 10):
  array = range(i)
  t = timer()
  function1(array)
  y.append(timer()-t)
  x.append(i)

plt.plot(x, y)
plt.show()
