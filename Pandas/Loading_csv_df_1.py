import pandas as pd
#Loading the results into dataframe
df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_public.csv')
schema_df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_schema.csv')
# print(df.shape)  #defines the structure of dataframe i,e m*n rows and columns 
# print(df.info())  #provides column level information
pd.options.display.max_columns
pd.set_option('display.max_columns',85)  #used to set the property of display

#to display top rows, default no of rows is 5 from
print(df.head())

#to display bottom rows, default no of rows is 5 from
print(df.tail())



