import numpy as np
"""
Stacks: Stack is used to join the sequence of elements along a new axis
thats is, if we give input 2d arrays, then stack will give a 3d array
if axis=0, elements of 2d will be joined along vertical way resulting in 3d array
if axis=1, elements will be joined along horizantal way resulting in 3d array
"""
#creating new 2dimensional arrays
a=np.arange(1,7).reshape(2,3)
b=np.arange(11,17).reshape(2,3)
stacked_arr=np.stack((a,b))  #elements will be joined along vertical way and default axis=0
print(stacked_arr)
print("===============")
stacked_arr=np.stack((a,b),axis=1)  #elements will be joined along vertical way and default axis=0
print(stacked_arr)

"""we have a function called hstack() which is used to stack the elements inthe horizantal way which is similar
to axis=1 which results in a 2d array which is similar to concatinate() with axis=1
"""
hstacked=np.hstack((a,b))
print(hstacked)
print("===============")
"""we have a function called vstack() which is used to stack the elements along vertical way which is similar
to axis=0 which results in a 2d array which is similar to concatinate() with axis==
"""
vstacked=np.vstack((a,b))
print(vstacked)
print("===============")

#we have a function called dstack() which is used to stack the elements along height or depth
#simply, rows will be converted to columns
dstacked=np.dstack((a,b))
print(dstacked)

