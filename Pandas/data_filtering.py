import pandas as pd
df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_public.csv',index_col='Respondent')
schema_df=pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\survey_results_schema.csv',index_col='Column')


#setting out the filter
high_sal=df['ConvertedComp'] >70000
columns=['Country','LanguageWorkedWith','ConvertedComp']
#print(df.loc[high_sal,columns])

#creating the list of countries, for which we want results
'''countries=['United States','india','United Kingdom','Germany','Canada']
fil=df.Country.isin(countries)
print(df.loc[fil & high_sal,'Country'])
'''

#creating filter, checking if the rows havings python in thier Language
#na=False means that any NaN (missing) values in the DataFrame will be treated as Fals
lang_fil=df['LanguageWorkedWith'].str.contains('Python',na=False) 
print(df.loc[lang_fil,'LanguageWorkedWith'].value_counts().count)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
people={
    'first_name':['santhosh','sunny'],
    'last_name':['kumar','kumar'],
    'email':['santhosh_kumar@gmail.com','Sunny_kumar@gmail.com']
}
df=pd.DataFrame(people,['a','b']) #insted of 0,1,2,3.. default index, im setting a,b,c,d as index
print(df)


l=['santhosh','sunny','bunny','sreeja']
df1=pd.DataFrame(l,columns=['Names'])
fil=(df1['Names']=='bunny')
print(df1[fil])

df = pd.read_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\data\nba.csv')
pd.options.display.max_rows = 1000
names_fil=(df["Name"].str.startswith('T') &  (df["Name"].str.contains('oh') | df["Name"].str.contains('fe',na='True') ))
#df_names=df[names_fil]
#fil_names=df_names["Name"].str.contains('oh')


print(df.loc[names_fil])
