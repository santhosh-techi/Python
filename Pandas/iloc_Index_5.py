import pandas as pd
#loading the results into dataframe
#now im making 'Respondent' as indexed column
df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_public.csv',index_col='Respondent')
schema_df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_schema.csv',index_col='Column')
pd.set_option('display.max_columns',85)
#print(schema_df.loc['Hobbyist','QuestionText'])

#sorting the index in asceding order
schema_df.sort_index(inplace=True)
#print(schema_df)

print(df.iloc[1,[0,1,2,3,4,5]])
print(schema_df.loc[['MainBranch','Hobbyist','OpenSourcer','OpenSource','Employment','Country'],'QuestionText'])
      

