import random as r

counter=1
name_list=[]
while True:
    name=input(f'Please enter the name{counter}: ')
    if name.isalpha():
        counter+=1
        name_list.append(name)
        if len(name_list)>=5:
            break

#select one random name who has to pay bill

length=len(name_list)
number=r.randint(0,length-1)
print(f'You have to pay bill for this time {name_list[number]}')