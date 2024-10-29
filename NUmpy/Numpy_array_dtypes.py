import numpy as np
#f represents float type, we can also provide following types
"""i: interger
   f: float
   c:complex
   b:boolean
   S: strings"""
array1=np.array((1,2,3,4,5),dtype='i') 

print(array1)
print(array1.dtype)

#For i, u, f, S and U we can define size as well 

array2=np.array([],dtype='i3')
print(array2.size)