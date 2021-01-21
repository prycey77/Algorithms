memo = {}
def fib_memo(n):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]
#print(fib_memo(800))

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))