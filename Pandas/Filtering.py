import pandas as pd
people={
    'first_name':['santhosh','sunny','Bunny'],
    'last_name':['kumar','',''],
    'Age':[27,27,23],
    'email':['santhosh_kumar@gmail.com','Sunny@gmail.com','Bunny@gmail.com']
}

df=pd.DataFrame(people)
#setting out the filter whose last name =kumar
Fil=(df.last_name=='kumar')
"""
print(df[Fil]) #here, we cannot simply use df.Fil, bcz df dont have Fil attribute
print(df[df.last_name=='kumar'])  # we can either set the filter inside
print(df.loc[Fil])  # we can also achive through loc[]

fil1=(df.first_name=='santhosh')
#when we want specific columnsb then
print(df.loc[fil1,['last_name','email']])
"""
#filtering people who's last name is null and age>23
fil=((df.last_name=='') & (df.Age>24))  # we cnt writr all the conidtions together
print(df[fil])
print(df[~fil]) #opposite for fil condition
