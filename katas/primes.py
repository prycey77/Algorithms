from math import sqrt, ceil

def find_primes(num):
    # If either num is less than 2 or number is even
    # Return Not prime
    if num < 2 or (num > 2 and num % 2 == 0):
        return 'Not prime'

    # Calculate the range to traverse, based on:
    # A number is not prime if it is divisible by
    # a number less or equal to the square root of the number
    r = ceil(sqrt(num))
    for i in range(3, r + 1):
        if num % i == 0:
            return 'Not prime'

    return 'Prime'

T = int(input())
nums = []
for _ in range(T):
    num = int(input())
    print(find_primes(num))
  