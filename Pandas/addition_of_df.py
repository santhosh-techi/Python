import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John'],
    'Last_Name':['Schafer','Doe','Smith'],
    'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com']
}
df=pd.DataFrame(dataset)
dataset1={
    'Last_Name':['Kumar','Sreeja'],
    'Email' :['SanthoshKumar@gmail.com','JangamSreeja@gmail.com']
}
df1=pd.DataFrame(dataset1)
#appending df and df1, we can use either axis=0 or ignore_index, sort will used to sort the columns in ascending
df_new=pd.concat([df,df1], ignore_index=True,sort=True) 

fil=df_new['First_Name']=='Jane'
df_new.loc[fil,'First_Name']='Corey'
print(df_new['First_Name'].unique)