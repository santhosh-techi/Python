import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John'],
    'Last_Name':['Schafer','Doe','Smith'],
    'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com']
}
df=pd.DataFrame(dataset)
#2. applymap: it is used to perform operation for all the elements of the dataframe,can be apply only on dataframes
#print(df.applymap(len)) #DataFrame.applymap has been deprecated.
#syntax : DataFrame.applymap(func)
print(df.applymap(len))
print(df.applymap(str.lower))
print(df.applymap(str.upper))
print(df.applymap(str.capitalize))
print(df.applymap(str.title))