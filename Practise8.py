import numpy as np
import pandas as pd
data={
    'ID':[101,102,np.nan, 104,105,106],
    'Age': [25,np.nan,35,42,np.nan,28],
    'Income': [55000,63000,np.nan,72000,48000,np.nan],
    'City': ['New York','Log Angeles','Chicago',np.nan,'San Franciso','Houston'],
    'Score': [88,np.nan,92,85,np.nan,91]
}
df=pd.DataFrame(data)
#print(df['Age'].mean())
#df['Age']=round(df['Age'].fillna(df['Age'].mean()))
#print(df.isnull().count())  #to check the no of missing values
#print(df.fillna({'ID':1,'Income': 10000,'City':'Hyderabad','Score': 100}))
print(df.bfill())