def fib(n):
    arr = [1, 1, 0]
    for i in range(n-2):
        arr.insert(0, arr[0] + arr[1])
    return arr[0]

print(fib(3))
print(fib(4))
print(fib(50))
