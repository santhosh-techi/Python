import pandas as pd

person={
    'first_name':['Corey','Jane','John'],
    'last_name':['Schrafer','Doe','Doe'],
    'email':['CoreyMSchrager@gmail.com','JaneDoe@gamil.com','JohnDoe@gamil.com']
}
#loading the dictionary into the dataset
df=pd.DataFrame(person)
#print(df)  #here, by default df provides the index values for each row
print('Setting the Index')
"""
Setting the Index: we have set_index() function, column name is passed to make as index column,
2. inplace attribute modifes the dataset
"""
df.set_index='first_name' #either we can give direct or else like below
df.set_index('first_name',inplace=True) #now im making the first_name as index value
#print(df)
print(df.loc['Corey'])  #now first_name is the indexed column in the dataframe

"""
Resetting the Index: we have reset_index() function, column name is passed to make as index column,
2. inplace attribute modifes the dataset
"""
print('Resetting the Index')
df.reset_index(inplace=True)
#print(df)

