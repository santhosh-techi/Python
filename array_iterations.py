import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

"""
op_types=['data type']: we can change the datatype of each elemenet while iteration, 
NumPy does not change the data type of the element in-place (where the element is in array), so to achive this
we need some other place called buffer which need to be passed to flags like flags=['buffered']
"""

arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): 
  print(x)

#we can also skip the elements using the step
# : before ',' representd select all the rows, 
# and ::2 represents, select every second column, starting from index 0."
for x in np.nditer(arr[ :, 2]): 
  print(x)

#some times, we need an index number of an element, so this can be achived using ndenumate()

for id,x in np.ndenumerate(arr):
  print(id,x)

arr1 = np.array([[1, 2, 3],[7,8,9]])

for co_ordinates, elements in np.ndenumerate(arr1):
    print(co_ordinates,elements)
  