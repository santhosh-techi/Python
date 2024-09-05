list1=[1,2,3,4,5,6,7,8,9,0]
Target=10

def sub_lists(array,target):
    length=len(array)
    sub_array=[]
    for i in range(length):
        sub_list=[]
        counter=0
        sub_list.append(array[i])
        for j in range(length):
            if array[i]!=array[j]:
                sub_list.append(array[j])
                if sum(sub_list)==Target:
                    sub_array.append(tuple(sub_list))
                    counter+=1

    return f'Number of possible ways are {counter} and the sub_lists are: {sub_array}'

print(sub_lists(list1,Target))

