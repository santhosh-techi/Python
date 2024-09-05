numbers=input('enter the numbers: ')
number_list=','.join(numbers)
number_list=number_list.split(',')

for i in range(len(number_list)):
    number_list[i]=int(number_list[i])
print(number_list)

max_num=0
for value in number_list:
    if value>max_num:
        max_num=value
print(max_num)

