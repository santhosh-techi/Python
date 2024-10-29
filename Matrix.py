import numpy as np
array_2d=[[10,20,30],[40,50,60],[70,80,90]]
print(array_2d)

#converting the list into array
matrix=np.array(array_2d)  #converting the list elements into array elements

res=matrix[1:3,0:2]  #slicing methods
print(res)