def recursive_factorial(n):
    if n == 2:
        return 2   
    return n*recursive_factorial(n-1)



def factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer

print(recursive_factorial(5))