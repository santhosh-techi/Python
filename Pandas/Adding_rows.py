import pandas as pd
dataset = {
    'First_Name': ['Corey', 'Jane', 'John'],
    'Last_Name': ['Schafer', 'Doe', 'Smith'], 
    'Email': ['CoreySchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnSmith@gmail.com']
}
df = pd.DataFrame(dataset)
# Create a new row 
new_row = pd.DataFrame([{'First_Name': 'Santhosh'}])
# Concatenate the new row to the existing DataFrame, we can use axis=0 in order to append and axix=1 in order to join
df = pd.concat([df, new_row],axis=0)#, ignore_index=True)
print(df)

#adding the last_name to the santhosh name
filt=df['First_Name']=='Santhosh'
df.loc[filt,['Last_Name','Email']]=('Kumar','SanthoshKumar@gmail.com')
print(df)

