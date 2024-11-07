import pandas as pd
def age_description(age):
    if age >=1 and age<=5:
        return 'Teenage'
    elif age>5 and age<=10:
        return 'Grown Teenage'
    elif age>10 and age<=18:
        return 'Matured'
    elif age>18 and age<42:
        return 'Married Age'
    else:
        return 'Old age'

df=pd.DataFrame({'Age':[5,10,12,15,20,27,30,55]})
df['Age_desciptions']=df['Age'].map(age_description)
print(df)