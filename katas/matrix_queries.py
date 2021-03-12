"""
You are given two numbers n and m representing the dimensions of 
an n × m rectangular board. The rows of the board are numbered from 
1 to n, and the columns are numbered from 1 to m. Each cell has a 
value equal to the product of its row index and column index 
(both 1-based); in other words, board[i][j] = (i + 1) * (j + 1).
Initially, all the cells in the board are considered active, though 
some of them will eventually be deactivated through a sequence of 
queries - specifically, you will be given an array queries, where 
each query is of one of the following 3 types:
[0] - find the minimum value among all remaining active cells on the 
board.
[1, i] - deactivate all cells in row i;
[2, j] - deactivate all cells in column j;
Given the dimensions n, m, and the array of queries, your task 
is to return an array consisting of calculated values 
(results of the queries of the 0th type), in the order in which 
they were calculated.

Example
For n = 3, m = 4, and queries = 
[[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]], 
the output should be matrixQueries(n, m, queries) = [1, 1, 2, 6].

[[1,2,3,4],
 [2,4,6,8],
 [3,6,9,12]
]
"""

def matrix_queries(n, m, queries):
    output = []
    matrix = [ [(j+1) * (i +1) for i in range(m)] for j in range(n)]
    for querie in queries:
        if len(querie) == 1:
            output.append(min(min(matrix)))
        else:
            if querie[0] == 1:
                for i in range(len(matrix[0])):
                    matrix[querie[1]-1][i] = float("inf") 
            if querie[0] == 2:
                
                for i in range(len(matrix)):
                    print(matrix[i][querie[1]-1])
                    matrix[i][querie[1]-1] = float("inf")


                

    print(matrix)
    print(output)      


queries = [[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]]
matrix_queries(3,4,queries)