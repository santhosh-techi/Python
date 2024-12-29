import pandas as pd
employee_df = pd.DataFrame({
    'Emp_Id': [101, 102, 103, 104, 105],
    'Emp_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
})
projects_df = pd.DataFrame({
    'Emp_Id': [101, 103, 104, 105, 106],
    'Proj_Name': ['Project_A', 'Project_B', 'Project_C', 'Project_D', 'Project_E']
})
#performing the inner join 
print(pd.merge(employee_df,projects_df,how='inner',on='Emp_Id'))

#performing the left join 
merged_df=pd.merge(employee_df,projects_df,how='left',on='Emp_Id')
print(merged_df[merged_df['Proj_Name'].notnull()])

# print(pd.merge(employee_df, projects_df, on='Emp_Id', how='cross'))
employee_df['key'] = 1
projects_df['key'] = 1

# Perform the merge on the key column
#print(pd.merge(employee_df, projects_df, on='key').drop('key', axis=1))

import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})
df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'city': ['New York', 'Los Angeles', 'Chicago']
})
# Merge DataFrames on the 'id' column
merged_df = pd.merge(df1, df2, on='id', how='inner').filter(items=['id','age']) 
#filyer the rows where age >25
fil=merged_df[merged_df['age']>25]
print(fil)