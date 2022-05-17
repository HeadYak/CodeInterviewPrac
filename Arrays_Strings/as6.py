from typing import List
from math import sqrt, floor


def rotateMatrix(matrix: List[List[int]]) -> List[List[int]]:

    N = len(matrix[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp



    return matrix



def printMatrix(matrix: List[List[int]]) -> None:
    size = len(matrix)

    if(floor(size) != size):
        print("Invalid matrix")

    i = 0

    while(i< size):
        j = 0

        while(j<size):
            print(matrix[i][j], end=' ')

            j+=1
        print("")

        i+=1









input = [[1,0,0],
         [0,0,0],
         [0,0,0]]

printMatrix(input)
print("\n")

print(printMatrix(rotateMatrix(input)))
