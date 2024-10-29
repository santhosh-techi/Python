import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\nba.csv')
pd.options.display.max_rows = 1000
names_fil=(df["Name"].str.startswith('T') &  (df["Name"].str.contains('oh') | df["Name"].str.contains('fe',na='True') ))
#df_names=df[names_fil]
#fil_names=df_names["Name"].str.contains('oh')


print(df.loc[names_fil])




