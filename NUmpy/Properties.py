import numpy as np

my_list=[1,2,3,4,5]
matrix_2d=np.array([[1,2],[3,4],[5,6]])
arr=np.array(my_list)

#to print the information
print('array elements: ',arr)
print('Size :',arr.size)
print('Datatype :',arr.dtype)
print('Dim :',arr.ndim)
print('Shape :',arr.shape)
print('Shape :',matrix_2d.shape)

print(matrix_2d.size)
print(matrix_2d)

array_list=np.array(my_list)

print(my_list,type(my_list))
print(array_list,type(array_list))

print(id(my_list), id(array_list))


