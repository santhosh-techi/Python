
import pandas as pd
people={
    'first_name':['santhosh','sunny'],
    'last_name':['kumar','kumar'],
    'email':['santhosh_kumar@gmail.com','Sunny_kumar@gmail.com']
}

df=pd.DataFrame(people)#loading into the dataframe
df.set_index('first_name',inplace=True) #setting out the index column as first_name
print(df.loc['sunny','email']) #accessing emial of sunny
print(df.loc['sunny','santhosh'],'email') #accessing 2 rows email id's
print(df.loc['sunny',['last_name','email']]) #accessing the multiple columns of a sinle row

print(df.index)
