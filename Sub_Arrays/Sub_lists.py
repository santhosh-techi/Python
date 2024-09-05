def sub_lists(l, Target):
    sub_list = []
    counter = 0
    list_len = len(l)
    
    for i in range(list_len):
        for j in range(list_len): 
            if l[i] + l[j] == Target:
                counter += 1
                sub_list.append((l[i], l[j]))
    
    return f'The number of possible matches are {counter} and the sub_list is: {sub_list}'

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Target = 11
print(sub_lists(l, Target))



