nam='santhosh kumar'
name=nam.replace(' ','')
print(name)
len_name=len(name)
print(len(name))
name1=[]
for i in range(len(name)):
    #temp_name=
    name1.append(name[len_name-1-i])
print(name1)
name2=''
for i in range(len(name1)):
    name2=name2+name1[i]
if name==name2:
    print(f'{name} and {name2} are same so they are palindrome')
else:
    print(f'{name} and {name2} are not same so they are not palindrome')

