"""
[0,3,4,31], [4,6,30] = [0,3,4,4,6,30,31]
"""

def merge_sorted_arrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    merged_array = []

    i, j = 0, 0 

    while i < len(arr1) and j <  len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            merged_array.append(arr2[j])
            j += 1


    return merged_array

print(merge_sorted_arrays([0,3,4,31], [4,6,30]))