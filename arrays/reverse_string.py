from decimal import Decimal
import time

def reverse_string(string):
    """Stupid way!"""
    string_array = list(string)
    end_pointer = len(string) - 1
    start_pointer = 0
    while end_pointer != start_pointer:
        temp = string_array[start_pointer]
        string_array[start_pointer] = string[end_pointer]
        string_array[end_pointer] = temp
        start_pointer += 1
        end_pointer -= 1
    return ''.join(string_array)

def reverse_string2(string):
    my_list = []
    for i in range(len(string)-1, -1, -1):
        my_list.append(string[i])
    return ''.join(my_list)

if __name__ == "__main__":
   
    methods = [reverse_string, reverse_string2]
    for m in methods:
        start = time.perf_counter()
        m('Hello world 123456789')
        end = time.perf_counter()
        print(Decimal((end - start)))


