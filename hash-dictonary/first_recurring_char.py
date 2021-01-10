#[1,2,3,4,5,2,3] returns 2

def first_recurring(array):
  memo = {}
  for num in array:
    if num not in memo:
      memo[num] = True
    else:
      return num

print(first_recurring([1,2,3,4,5,2,3]))