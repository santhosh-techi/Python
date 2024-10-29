"""
Joining NumPy Arrays:
Joining means putting contents of two or more arrays in a single array.
We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. 
If axis is not explicitly passed, it is taken as 0.
Concatination of arrays is similar to join of tables in sql
we join sequel tables using key column, in numpy we join using axis
"""
import numpy as np
#1D Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr=np.concatenate((arr1,arr2),axis=0) ##1d arrys will join in horizantal way
print(arr)

#2D Array
arr1 = np.array([[1, 2, 3],[4,5,6]])
arr2 = np.array([[7, 8, 9],[10,11,12]])

arr_new1 = np.concatenate((arr1, arr2),axis=0) #vertical way, i,e along y axis
arr_new2 = np.concatenate((arr1, arr2),axis=1) #vertical way, i,e along x axis
print(arr_new1)
print(arr_new2)