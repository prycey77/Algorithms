import time
from decimal import Decimal

"""
Find a pair of numbers in array that add to pair_sum.
"""


def has_pair_total_sum1(array, pair_sum):
    """Has O(n^2) time complexity"""
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == pair_sum:
                return True
    return False

def has_pair_total_sum2(array, pair_sum):
    """Has O(n) time complexity"""
    number_set = set()
    for number in array:
        if number in number_set:
            return True
        number_set.add(number)
    return False

if __name__ == '__main__':
    array = [6,4,10,11,1,7]
    
    methods = [has_pair_total_sum1, has_pair_total_sum2]

    for m in methods:
        start = time.perf_counter()
        m(array, 9)
        end = time.perf_counter()
        print(Decimal((end - start)))
