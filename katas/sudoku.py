"""
Implement an algorithm that will check whether the given grid of numbers 
represents a valid Sudoku puzzle according to the layout rules described above. 
Note that the puzzle represented by grid does not have to be solvable.
"""


def sudoku(grid):
    for i in range(9):
        if _check_nums(grid[i]) == False:
            return False
        col = []
        for j in range(9):
            col.append(grid[j][i])

        if _check_nums(col) == False:
            return False
    for T in range(0,9,3):
        for x in range(0,9,3):          
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(grid[i+T][j+x])
                if _check_nums(box) == False:
                    return False
    return True

def _check_nums(arr):
    for num in arr:
                if num.isdigit():
                    if arr.count(num) > 1:
                        return False
