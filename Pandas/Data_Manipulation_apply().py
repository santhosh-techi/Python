import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John'],
    'Last_Name':['Schafer','Doe','Smith'],
    'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com']
}
df=pd.DataFrame(dataset)
#we have 4 methods for performing data manipulation and they are apply,map, applymap and replace
#1. apply method: It is used to call a function over the series values and below are the examples
print(df['Email'].apply(str.lower)) #converting all the email address to the lower case
print(df['Email'].apply(len)) #finding the length of all email addresses

#creating a user defined function, for converting the first_name to upper case
def df_upper_case(Name):
    return Name.upper()

df['First_name'].apply(df_upper_case) #calling user function
print(df.apply(pd.Series.min)) #we can also apply series methods in the apply method
print(df.apply(pd.Series.max))



