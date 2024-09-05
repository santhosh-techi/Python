names=[{'name1':'santhosh','age1':12},{'name2':'Sunny','age2':13},{'name3':'Bunny','age3':14}]

for person in names:
    for key,value in person.items():
        #print(key,value)
        if 'name' in key:
            name=value
        elif 'age' in key:
            age=value
    print(f'Name is {name} and Age is {age}')

#second Type

Details=[{'name':'santhosh','age':12},{'name':'Sunny','age':13},{'name':'Bunny','age':14}]

for sub_dic in Details:
    print(f"Name is '{sub_dic['name']}' and age is '{sub_dic['age']}'") 




 