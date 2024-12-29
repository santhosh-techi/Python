import pandas as pd
iphone_models={
    'Models': ['16 Pro Max','16 Pro','16'],
    'Launch_Year':[2024,2024,2023]
}
samsung_models={
    'Models': ['S24','S23','S22'],
    'Launch_Year':[2024,2023,2023]
}
df1=pd.DataFrame(iphone_models)
df2=pd.DataFrame(samsung_models)
Mobiles=pd.concat([df1,df2],ignore_index=True,axis=1)
print(Mobiles.T.drop_duplicates())


students = {
    'students_names': {
        'Std_Name': ['santhosh', 'sunny'],
        'Std_class': [10, 9]
    },
    'students_location': {
        'Std_location': ['Hyderabad', 'Kamareddy'],
        'Std_District': ['Hyderabad', 'Kamareddy'],
        'Std_Pincode': ['123', '321']
    }
}
# Create a DataFrame from the flattened dictionary
df_names = pd.DataFrame(students.get('students_names'))
df_location = pd.DataFrame(students['students_location'])

# Combine the DataFrames
df = pd.concat([df_names, df_location],axis=1)
print(df)

