import pandas as pd
df = pd.read_excel(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\Employee_Dept.xlsx', sheet_name=['Employees', 'Department'])
Employee_df = df['Employees']
Department_df = df['Department']
Employee_df.columns = Employee_df.columns.str.strip()
Employee_df['hire_date']=pd.to_datetime(Employee_df['hire_date'])
Department_df.columns = Department_df.columns.str.strip()
emp_dept_df=pd.merge(Employee_df,Department_df,how='outer',on='Dept_No')

#count of employees
print(Employee_df.__len__()) # len(Employee_df)
#sorting   the dataframe based on the salary descending
print(Employee_df.sort_values(by='salary',ascending=False))
#aggregation of salaries
print(f'average salary is: {Employee_df["salary"].mean()}')
print(f'Maximun salary is: {Employee_df["salary"].max()}')
print(f'Minimun salary is: {Employee_df["salary"].min()}')
print(f'Sum of salary is: {Employee_df["salary"].sum()}')
print(Employee_df['Dept_No'].unique()) # unique dept no
#salaries higher than 4500
print(Employee_df[Employee_df['salary']>4500])
#employees name starting with J
print(Employee_df[Employee_df['emp_name'.lower()].str.startswith('J')])
#employees who dept_name is accounting or sales
print(emp_dept_df[['emp_id','emp_name']][(emp_dept_df['Dept_Name']=='Accounting') | (emp_dept_df['Dept_Name']=='Sales')])
#employees count who dept_name is accounting or sales
print(len(emp_dept_df[['emp_id','emp_name']][(emp_dept_df['Dept_Name']=='Accounting') | (emp_dept_df['Dept_Name']=='Sales')]))
#employees salary between 2000 and 5000
print(Employee_df[['emp_id','emp_name','salary']][(Employee_df['salary']>=2000) & (Employee_df['salary']<=5000)])
#select 3 employees in the Research department
print(emp_dept_df[emp_dept_df['Dept_Name']=='Research'].head(3))
#sum of the salary of employees in the sales dept
print(f'Summation of salary is:{emp_dept_df["salary"][emp_dept_df["Dept_Name"]=="Sales"].sum()}')
#names and length of the names 
Employee_df['emp_names_len']=Employee_df['emp_name'].apply(len) #creating new filed as name length
print(Employee_df[['emp_name','emp_names_len']])
#first three characters of emp_names
Employee_df['first_3_chars']=Employee_df['emp_name'].str.slice(0,3)
print(Employee_df[['emp_name','first_3_chars']])
#Concatenate the Name and Department columns and rename the result as EmployeeInfo
Employee_df['EmployeeInfo']=Employee_df['emp_name']+'_'+(Employee_df['Dept_No'].astype(str))
print(Employee_df['EmployeeInfo'])
#print the emp_names by removing any spaces available
print(Employee_df['emp_name'].str.strip())
#print the emp details who name is adams or james
print(Employee_df[Employee_df['emp_name'].str.lower().isin(['james','adams'])])
#sum of salaries based for each dept
print(Employee_df.groupby('Dept_No')['salary'].sum())
print(Employee_df.groupby('job_name')['salary'].sum())
#depart name is not present in emp table
print(emp_dept_df['Dept_Name'][emp_dept_df['emp_id'].isnull()])
dept_with_employees = Employee_df['Dept_No'].unique()
departments_without_employees = Department_df[~Department_df['Dept_No'].isin(dept_with_employees)]
print(departments_without_employees)
#print details of the emps whose ename contains ‘a’.
print(Employee_df[Employee_df['emp_name'].str.contains('a',case=False)])
#print details of the emp whose ename ends with ‘h’ and contains six alphabets.
filter_df=((Employee_df['emp_name'].str.lower().str.endswith('h')) & (Employee_df['emp_name'].apply(len)==5))
print(Employee_df[filter_df])
#print details of the emps who have joined in Feb’2014.
print(Employee_df[((Employee_df['hire_date'].dt.year==1981) & (Employee_df['hire_date'].dt.month==2) )])
#get the job wise count of members with more than 3
#job_wise_grp=Employee_df.groupby('job_name').size()  #size is used to get the count of batch 
job_wise_grp=Employee_df.groupby('job_name').apply(len) 
print(job_wise_grp[job_wise_grp>=3])











