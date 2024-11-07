import pandas as pd
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

