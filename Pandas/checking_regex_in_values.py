import pandas as pd
import re as rg
df=pd.read_csv(r"C:\Users\jangasa\Downloads\ProcessedOrders_NOV-pretest SBX 1-13-25.csv",dtype=str)
cl_order_code=df['Order Code'].fillna('')
pattern=r"[!$%^&*()[\]{}~<>+=]"
mask = cl_order_code.str.contains(pattern, regex=True).value_counts()
print(mask)
counter=0
#for id, value in cl_order_code[mask].items():
 #   counter+=1
    #print(id, value)

#print(counter)

arr=[1,13,2,12,2,11,-12,2,-1,2,2,11,12,2,-6,2,2,2,2,2,2,2]
max_count={'Max_Count_value': 0}
unique_set=set(arr)
for element in unique_set:
    count=0
    for index_val in range(len(arr)):
        if element == arr[index_val]:
            count=+1
    if max_count['Max_Count_value']<count:
        max_count['Max_Count_value']=count

print(max_count['Max_Count_value'])