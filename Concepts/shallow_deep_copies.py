import copy as c
list1=[[1,2],[3,4],[5,6]]

ref1=list1
print(id(ref1),id(list1))  #objects are same with 2 different names

#creating a shallow copy
shallow_copy=c.copy(list1)  #it creates the new object with referecing the orginal object
print(id(list1),id(shallow_copy))  # creates a new object with diff reference, but inner obejct references are same
print(id(list1[0]),id(shallow_copy[0]))

shallow_copy[0].append('santhosh')
print(list1,shallow_copy)
print(id(list1[0]),id(shallow_copy[0]))

#creating deepcopy
deep_copy=c.deepcopy(list1)  #it creates a new objects with no reference to the orginal one
deep_copy[0].append('sunny')
print(id(list1[0]),id(shallow_copy[0]),deep_copy[0])
#ref of inner objects

print(id(ref1[0]),id(shallow_copy[0]),id(deep_copy[0])) 
