import pandas as pd
df = pd.read_excel(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\Employee_Dept.xlsx', sheet_name=['Employees', 'Department'])
Employee_df = df['Employees']
Department_df = df['Department']
Employee_df.columns = Employee_df.columns.str.strip()
Employee_df['hire_date']=pd.to_datetime(Employee_df['hire_date'])
Department_df.columns = Department_df.columns.str.strip()
emp_dept_df=pd.merge(Employee_df,Department_df,how='outer',on='Dept_No')
dept_names=['Accounting','Sales']
filt=emp_dept_df[emp_dept_df['Dept_Name'].isin(dept_names)]
max_salary_dept=filt.groupby('Dept_Name')['salary'].max()
print(max_salary_dept)
