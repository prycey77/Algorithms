"""
Given five positive integers, find the minimum and maximum 
values that can be calculated by summing exactly four of the 
five integers. Then print the respective minimum and 
maximum values as a single line of two space-separated long 
integers.

Example

arr = [1,3,5,7,9]

16 24
"""

def mini_max(list):
    list.sort()
    min = 0
    max = 0
    for i in range(len(list) - 1):
        min += list[i]
    for i in range(1, len(list)):
        max += list[i]
    print(min, max)

mini_max([1,3,5,7,9])