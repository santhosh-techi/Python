my_tuple=(1,2,'a',"sunny","A",True)
int_list=[]
bool_list=[]
string_list=[]
for i in my_tuple:
    if type(i)==int:
        int_list.append(i)
    elif type(i)==bool:
        bool_list.append(i)
    else:
        string_list.append(i)

print(int_list)
print(bool_list)
print(string_list)
print(tuple(int_list))