# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

import pandas as pd
people={
    'first_name':['santhosh','sunny'],
    'last_name':['kumar','kumar'],
    'email':['santhosh_kumar@gmail.com','Sunny_kumar@gmail.com']
}

df=pd.DataFrame(people)
#creating the first_name field as index and by using inplace=true, changes the orginal file
df.set_index('first_name',inplace=True)
print(df.loc['sunny',['last_name','email']])

print(df.index)

