import pandas as pd
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Math': [90, 88],
    'Science': [88, 92],
    'History': [75, 80]
})

df2 = pd.DataFrame({
    'Name': ['Charlie', 'David'],
    'Age': [35, 28],
    'Math': [78, 92],
    'Science': [85, 90],
    'History': [70, 85]
})
concat_df=pd.concat([df1,df2],ignore_index=True)
print(concat_df)

