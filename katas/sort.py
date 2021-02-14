'''
Input           | output
[2,0,2,1,1,0]   | [0,0,1,1,2,2]
'''

def sort(list):
    red_count = white_count = blue_count = 0

    for i in list:
        if i == 0:
            red_count += 1
        if i == 1:
            white_count +=1
        if i == 2:
            blue_count += 1

    if red_count > 0:
        for i in range(red_count):
            list[i] = 'red'
    
    if white_count > 0:
        for i in range(white_count):
            list[i+red_count] = 'white'
    
    if blue_count > 0:
        for i in range(blue_count):
            list[i + (white_count + red_count)] = 'blue'
    return list




print(sort([2,0,2,1,1,0]))

print(sort([2,0,2,0])) # [0,0,2,2]

print(sort([0,0]))

print(sort([2,2,1,1,0,0]))

print(sort([2,2,2,2,1,2,0]))