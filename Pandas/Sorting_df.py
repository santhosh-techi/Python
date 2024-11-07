import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John','Jane'],
    'Last_Name':['Schafer','Doe','Smith','Adam'],
    'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com','JaneAdam@gamil.com']
}
df=pd.DataFrame(dataset)

dataset1={
    'Last_Name':['Kumar','Sreeja'],
    'First_Name':['Santhosh','Jangam'],
    'Email' :['SanthoshKumar@gmail.com','JangamSreeja@gmail.com']
}
df1=pd.DataFrame(dataset1)
df_new=pd.concat([df,df1],ignore_index=True,sort=True)
#sorting the new df with with asceding order on first_name
sorted_df=df_new.sort_values(by='First_Name')
#print(sorted_df)

#sorting the df in descending order
desc_df=df_new.sort_values(by='First_Name',ascending=False)
#print(desc_df)

#we can also sort order by multiple fileds in the form of lists
mult_sort_df=df_new.sort_values(by=['First_Name','Last_Name'],ascending=False)  #we can pass ascending=[False,True]
#in order to make it permanent we need to pass inplce=true
#print(mult_sort_df)

#we can also sort the values based on the index using df.sort_index()
print(mult_sort_df.sort_index())