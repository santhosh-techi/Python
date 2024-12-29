#stack dataframe: it is used to stack the data, that is placing something on top of existing one 
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22, 23, 24],
    'Math': [90, 88, 95],
    'Science': [88, 91, 89],
    'History': [75, 78, 80],
    'English': [85, 87, 86],
    'Physics': [92, 89, 90],
    'Chemistry': [78, 79, 84]
})
stacked_df=df.stack()
#print(stacked_df)

#for reverting the changes
df=stacked_df.unstack()
#print(df)

#if dont want to touch any columns then
df.set_index(['Name','Age'],inplace=True)
print(df.stack())
