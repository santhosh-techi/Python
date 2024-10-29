import numpy as np

"""
The best way to change the datatype of an array is to make the copy of an existing array by using the astype()
astype('parameter') is used to create the copy of an existing array and make the change of datatype
paramter will be like i or int, bool or b, float or f,S of string

"""

arr = np.array([1.1, 0.0, -3.1])

newarr = arr.astype('bool')

print(f'the old arrays is: {arr} and the new arrays is {newarr}')
print(f'the old array type  is: {arr.dtype} and the new array type is {newarr.dtype}')