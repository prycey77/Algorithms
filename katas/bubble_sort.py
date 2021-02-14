def bubble_sort(input):
    for i in range(len(input)):
        for i in range(len(input) - 1):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
    return input
        

print(bubble_sort([1,3,6,2,3]))