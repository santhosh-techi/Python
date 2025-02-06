import pandas as pd
df=pd.read_csv(r"C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\pivot_example.csv")
#piviting the data
print(df)

#columns: defines on which field we want to perform pivot, values: defines which sector need to be shown
pivot_data=df.pivot(index='Date',columns='City',values='Temperature')
print(pivot_data)