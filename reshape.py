"""
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change number of elements in each dimension
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #we have 12 elements now
#changing from 1 dimension to 2 dim with 4rows 3 columns   4*3=12, so it will be possible
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #we have 12 elements
newarr = arr.reshape(2, 3, 2)  #changing to 3d 2*3*2=12 elements we have 
print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) #we have 8 elements
# newarr = arr.reshape(3, 3)  #we are reshaping to 2d with 3*3=9 elements, which is not possible so it will raise error
# print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

"""
We are allowed to have one "unknown" dimension.
Meaning that we do not have to specify an exact number for one of the dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.
Note: We can not pass -1 to more than one dimension.
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#Flattening the arrays: converting the multidimensional array into 1d dimensional array
#this can be achived by using the reshape(-1) function
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)