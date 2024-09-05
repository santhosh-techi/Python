arr=[2,3,1,2,4,3]
key=7

def minimal_sub_array(arr,key):
    n=len(arr)
    min_sub_array_len=int(len(arr))
    min_sub_list=[]
    for i in range(n):
        sub_list=[]
        #sub_list.append(arr[i])
        for j in range(i,n):
            sub_list.append(arr[j])
            if sum(sub_list)==key:
                if len(sub_list)<=min_sub_array_len:
                    min_sub_list=[]
                    min_sub_list.append(tuple(sub_list))
                    min_sub_array_len=int(len(sub_list))
            
      
    return f'the minimal length of sub array is: {min_sub_array_len} and the sub array is: {min_sub_list}'

print(minimal_sub_array(arr,key))

                