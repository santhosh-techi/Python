"""
Lists are used to store multiple items in a single variable.
Lists are created using square brackets:
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""
#Example for creating a list
thislist1 = ["apple", "banana", "cherry"]
print(thislist1)
#list items are indexed, so we can access them by their index value
print(thislist1[1])#it will print the item which has an index of 1, ie, banana
#we can also access the list items with the negative index value, index index starts from the -1 and starts from the list end item
#from the above list, printing the cherry item with the negative index
print(thislist1[-1],thislist1[-3])
"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#if the starting value is missed, the the start value will be from 0
print(thislist[:2])
#if the ending value is missed, then the last value will the end index value
print(thislist[2:])

