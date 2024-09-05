list1=[0,5,6,1,-1,7,3,9]
Target=6

def sub_lists(array,target):
    length=len(array)
    sub_array=[]
    counter=0
    for i in range(length):
        sub_list=[]

        sub_list.append(array[i])
        for j in range(i,length):
            if array[i]!=array[j]:
                
                if sum(sub_list)==Target:
                    sub_array.append(tuple(sub_list))
                    counter+=1
                    break
                sub_list.append(array[j])

    return f'Number of possible ways are {counter} and the sub_lists are: {sub_array}'

print(sub_lists(list1,Target))
