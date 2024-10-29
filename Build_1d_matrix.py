import numpy as np

n=int(input('enter the size of matrxi :'))
matrix=np.ndarray(shape=n,dtype=int)
for element in range(n):
    matrix[element]=input()

print(matrix)