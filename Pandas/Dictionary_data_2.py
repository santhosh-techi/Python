import pandas as pd
people={
    'first_name':['santhosh','sunny'],
    'last_name':['kumar','kumar'],
    'email':['santhosh_kumar@gmail.com','Sunny_kumar@gmail.com']
}

#loading dictionary dataset into dataframe, inorder to achieve this, we need to use DataFrame constructor
df=pd.DataFrame(people)
print(df)

#to read only specific keys, we can access the data either with bracket '[]' notation or  with dot '.' notation
print(df['email'])  # or: print(df.email)

#to get range of columns, we need to pass the column names in the form of list
column_names=['first_name','email']
print(df[column_names])

#to get the list of columns in the dataset
print(df.columns)



