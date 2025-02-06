import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
    'Score': [88, 92, 85, 88, 92, 92]
}
df = pd.DataFrame(data)
# Step 1: Assign rank based on 'Score' and 'Name' columns, keep rank of first occurrence
df['Rank'] = df.groupby('Name')['Score'].rank(method='first', ascending=False)
print(df)
# Step 2: Filter rows to keep only the first occurrence of each duplicate 'Name'
df_no_duplicates = df[df['Rank'] == 1].drop(columns='Rank')

#print(df_no_duplicates)
