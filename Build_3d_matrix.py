import numpy as np
matrix=np.ndarray(shape=(3,3,3),dtype=int)
print('Enter {matrix.size} elements ')
var=1

i,j,k=matrix.shape[0],matrix.shape[1],matrix.shape[2]

for m in range(i):
    for n in range(j):
        for z in range(k):
            matrix[m][n][z]=var
            var+=1

print(matrix[1][1][0])