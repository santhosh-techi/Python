import numpy as np

try: 
    m=int(input('Enter the size of rows : '))
    n=int(input('Enter the size of columns : '))
    matrix=np.ndarray(shape=(m,n),dtype=int)
    print('Enter the int type elements into an array ')
    if type(m)==int and type(n)==int:
        for row in range(m):
            for column in range(n):
                matrix[row][column]=input()
        print(matrix)
    else:
        raise ValueError
except ValueError as v:
    print(f'wrong values been entered {v}')

