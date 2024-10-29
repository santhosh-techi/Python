import pandas as pd
people={
    'first_name':['santhosh','sunny'],
    'last_name':['kumar','kumar'],
    'email':['santhosh_kumar@gmail.com','Sunny_kumar@gmail.com']
}
df=pd.DataFrame(people)
#print(df.columns)

#we can also rename all the fields using string functions, below are the examples
df.columns=[x.upper() for x in df.columns]
df.columns=[x.lower() for x in df.columns]
df.columns=[x.capitalize() for x in df.columns]
df.columns=[x.title() for x in df.columns]
df.columns=[x.replace('_','') for x in df.columns]
#print(df.columns)

#renaming the column using df.rename(columns={'old_column':'new_column'}), and to change in the Org dataframe use "inplace=True"
df.rename(columns={'First_Name':'F_Name','Last_Name':'L_Name','Email':'Email'},inplace=True)  
#print(df.columns)

""" Updating the single row value"""

df.loc[1]=('abc','abc','123') # no of columns need to be match, else it will raise an error

#changing particular row value, chanfing the email address of sunny
df.loc[1,'LastName']='abc'  # we can modify the respective filed values using df.at function
df.at[1,'LastName']='abc' 

#we can also mofified list of columns
df.loc[1,['FirstName','Email']]=('ABCD',1234)

#df.iloc[1,2]='abc'  # we can modify the respective filed valie

#using filters also we can achieve this
filt=df['FirstName']=='santhosh'
df.loc[filt,'FirstName']='abcd@gmail.com'

"""Updating the Multiple Rows"""
df['Email']=df['Email'].str.upper() #need to assign the filed to the respective field
print(df)

