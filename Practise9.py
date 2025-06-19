import numpy as np
import pandas as pd
data={
    'ID':[101,102,np.nan, 104,105,106],
    'Age': [25,np.nan,35,42,np.nan,28],
    'Income': [55000,63000,np.nan,72000,48000,np.nan],
    'City': ['New York','Log Angeles','Chicago','New York','San Franciso','Houston'],
    'Score': [88,np.nan,92,85,np.nan,91]
}
df=pd.DataFrame(data)
df.fillna({'ID':0,'Age': 18,'Income': 0.0, 'City': 'Hyderabad','Score': 0}, inplace=True)
grp_city=df.groupby(by='City').agg(Count=('City','size')).reset_index()
print(grp_city[grp_city['Count']==1])
#print(grp_city[['ID','City']].filter(lambda x: len(x)==1).reset_index())
#print(grp_city.groups)