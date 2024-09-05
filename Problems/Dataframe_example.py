import pandas as pd
#sample student data

data={
    'Name':['santhosh','sunny','bunny','sreeja'],
    'Grade':[100,99,98,97],
    'Attendence':[True,True,False,False]
}

#create dataframe
df=pd.DataFrame(data)
print(df.align)

