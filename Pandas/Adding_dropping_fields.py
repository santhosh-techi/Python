import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John'],'Last_Name':['Schafer','Doe','Smith'], 'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com']
}
df=pd.DataFrame(dataset)
#Adding a new column called Age With empty values
df['Age']=''

#Updating age of the person who's First name contains J in their name
filt=df['First_Name'].str.contains('J')
df.loc[filt,'Age']=25

#adding Name, which is the combination of firstname and lastname
df['Full_Name']=df['First_Name']+' '+df['Last_Name']
#or 
df['Full_Name1']=df['First_Name'].str.cat(df['Last_Name'],sep=' ')
print(df)

#dropping the columns: we've a function called drop(columns='Column_Name') which is used to drop the columns, 
# we can also drop list of columns as well
df.drop(columns=['Full_Name1'],inplace=True)
print(df)
#dropping columns first_name and last_name
df.drop(columns=['First_Name','Last_Name'],inplace=True)
print(df)

#we have a stf function called split, which is used to split the values of the fields, and need to use expand=True 
# to represent like df and assign the values to fields
df[['F_Name','L_Name']]=df['Full_Name'].str.split(' ',expand=True)
print(df)

