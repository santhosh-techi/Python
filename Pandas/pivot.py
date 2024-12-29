import pandas as pd
df=pd.read_csv(r"C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\pivot_example.csv")
#piviting the data
print(df)

#columns: defines on which field we want to perform pivot, values: defines which sector need to be shown
pivot_data=df.pivot(index='Date',columns='City',values='Temperature')
print(pivot_data)

#-------------------------------------------------------------#
df =pd.DataFrame( {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C','C'],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb','Feb'],
    'Quantity_Sold': [100, 120, 95, 110, 130, 100,200],
    'Revenue': [5000, 6000, 4500, 5500, 7000, 4800,4900]
})
#pivot_df = df.pivot(index='Product', columns='Month', values=['Quantity_Sold', 'Revenue'])
#pivot_df = pivot_df.sort_index(axis=1,ascending=False)# Reorder columns to have 'Jan' first
#print(pivot_df) it will throw an error

"""
1.Pivot_Table can handles duplicates
"""
pivot_table_df = df.pivot_table(index='Product', columns='Month', values=['Quantity_Sold', 'Revenue'],aggfunc='sum')
#aggfunc: will provide the aggregation

pivot_table_df = pivot_table_df.sort_index(axis=1,ascending=False)# Reorder columns to have 'Jan' first
print(pivot_table_df) # it will give the mean of duplicated data
