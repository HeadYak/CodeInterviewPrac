from math import floor
from typing import List


def zeroMatrix(matrix: List[List[int]]) -> List[List[int]]:
    size = len(matrix)


    i = 0
    j = 0
    rows = []
    cols = []

    while(i<size):
        j = 0
        while(j<size):
            if(matrix[i][j] == 0):
                rows.append(i)
                cols.append(j)



            j+=1
        i+=1


    matrix = zeroCol(matrix, cols)

    matrix = zeroRow(matrix, rows)


    return matrix





def zeroCol(matrix: List[List[int]], cols: List[int])-> List[List[int]]:

    i = 0

    for col in cols:
        i = 0
        while(i < len(matrix)):

            matrix[i][col] = 0

            i+=1


    return matrix



def zeroRow(matrix: List[List[int]], rows: List[int]) -> List[List[int]]:

    i = 0

    for row in rows:
        i = 0
        while(i < len(matrix)):
            matrix[row][i] = 0

            i+=1
    return matrix


def printMatrix(matrix: List[List[int]]) -> None:
    size = len(matrix)

    if(floor(size) != size):
        print("Invalid matrix")

    i = 0

    while(i < size):
        j = 0

        while(j < size):
            print(matrix[i][j], end=' ')

            j += 1
        print("")

        i += 1



input = [[1, 3, 4],
         [5, 1, 9],
         [1, 5, 0]]


printMatrix(zeroMatrix(input))
# data = [
#      ([
#          [1, 2, 3, 4, 0],
    #          [6, 0, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 0, 18, 19, 20],
#          [21, 22, 23, 24, 25]
#      ], [
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [11, 0, 13, 14, 0],
#          [0, 0, 0, 0, 0],
#          [21, 0, 23, 24, 0]
#      ])
#     ]
