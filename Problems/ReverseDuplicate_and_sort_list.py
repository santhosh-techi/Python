list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4]
list1=list.copy()
#creating a new list to adding into it to check the multiple existance of an element
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
    else:
        list.remove(i)
print(f'after removong the duplicates the new list is: {new_list}')
print(f'before sorting the orginal list: {list1}')


for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[j]
            list[j]=list[i]
            list[i]=temp
print(list)

if list ==new_list:
    print(1)

    








