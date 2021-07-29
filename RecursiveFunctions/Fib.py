def fibMem(n, mem={}):
    if n in mem:
        return mem[n]
    if n <= 1:
        return 1
    mem[n] = fibMem(n-1, mem) + fibMem(n-2, mem)
    return mem[n]

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fibMem(50))
print(fib(50))
