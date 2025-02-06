import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
    'Score': [88, 92, 85, 88, 92, 92],
    'Age': list(range(20, 26)) 
}
df = pd.DataFrame(data)
df['rank']=df.groupby('Name')['Score'].rank(method='first')
df.sort_values(by='Name',ascending=True,inplace=True)
df.drop(df[df['rank'] > 1].index,inplace=True)
# Reset the index
df.reset_index(inplace=True,drop=True)
print(df)

