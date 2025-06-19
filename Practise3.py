import pandas as pd
# Define the data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
    'Score': [88, 92, 85, 88, 92, 92],
    'Age': list(range(20, 26)) 
}
df = pd.DataFrame(data)
df['rank']=df.groupby('Name')['Score'].rank(method='first')
print(df.sort_values(by='Score',ascending=True))



