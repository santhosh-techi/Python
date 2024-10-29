import numpy as np

"""
1. The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.
2.The copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.
    a: Copy of an array can be done using array.copy() which cretaes a new copy,
and doesnt effects the orginal array if changes are done
3.The view does not own the data and any changes made to the view will affect the original array, 
and any changes made to the original array will affect the view,
    a: View of an array can be done using array.View() which creates a new copy,
and effects the orginal array if changes are done
"""

#Example of copy() method:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()  #making a copy of an array arr which creates a new array in x
arr[0] = 42  #changing the orginal array, which wont effect the new array x
print(f'The original array is :{arr} and the new array is : {x}')

#Example of View() method:
y=arr.view() #stroring the reference of original array
y[0]='10'  #changing the new array
print(f'The original array is :{arr} and the new array is : {y}') #changes will be reflecting both the arrays

"""
1. As using copy() we are creating the new array, so it own the data, 
whereas using view() just we are refering to the orginal array instead of creating the new array, 
so it wont owns the data.
2. In order to check this, we have a in-build property called base, which returns none if it owns the data else returns
the original arrays incase if it doesnt owns the data
"""
#Example using base function, as in the above line, we have createad a copy() of arr in x and view() in y

print(f'the base of copy() method is: {x.base} and for the view() is {y.base}')
