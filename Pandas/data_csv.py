import pandas as pd
import numpy as np
file=r'C:\Users\jangasa\Downloads\data.csv'
df=pd.read_csv(file)
pd.options.display.max_rows=1000 #setting the display size for rows to 1000
x,y=df.shape
#print(df.dropna().to_string())  #dropna is used to remove the empty cell rows, which returns the new dataframe
print(df.columns)
#['Duration', 'Pulse', 'Maxpulse', 'Calories']
fil=(df['Calories'].isna()) 
sum=(df['Calories'].sum(0))
