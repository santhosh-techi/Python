#melt dataframe: it is used to transform or reshape the df, wide df to long df
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [90, 85, 78, 92, 88],
    'Physics': [88, 92, 84, 91, 89],
    'Chemistry': [78, 89, 80, 87, 82],
    'Biology': [95, 93, 88, 94, 90],
    'History': [87, 91, 75, 89, 86]
})
melt_df=pd.melt(df,id_vars=['Name'],var_name='Subject',value_name='Marks').sort_values(by='Name',ascending=True)
print(melt_df)