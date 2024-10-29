import pandas as pd
#Loading the results into dataframe
df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_public.csv')
schema_df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_schema.csv')

#printing only 1st 2 rows and 4 columsn

rows=[0,1]
columns=[0,1,2,3]
print(df.iloc[rows,columns])  #iloc, we need to pass indices, for loc we need to pass lables

# for i in range(6):
#     print(df['Hobbyist'][i])

#to get the count of different values, we have a function calles value_counts()
print(df['Hobbyist'].value_counts())
print(df.loc[0,'Hobbyist'])

#we can also pass slicing arguemets
print(df.loc[0:2,'Hobbyist':'Country'])  #here last value in included