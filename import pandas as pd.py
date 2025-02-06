import pandas as pd
import re as rg
df=pd.read_csv(r"C:\Users\jangasa\Downloads\ProcessedOrders_NOV-pretest SBX 1-13-25.csv",dtype=str)
cl_order_code=df['Order Code'].fillna('')
pattern=r"[!$%^&*()[\]{}~<>+=]"
mask = cl_order_code.str.contains(pattern, regex=True)
counter=0
for id, value in cl_order_code[mask].items():
    counter+=1
    #print(id, value)

print(counter)