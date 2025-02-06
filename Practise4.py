import pandas as pd
dataset = {
    'First_Name': ['Corey', 'Jane', 'John'],
    'Last_Name': ['Schafer', 'Doe', 'Smith'],
    'Email': ['CoreySchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnSmith@gmail.com']
}
df = pd.DataFrame(dataset)
df['Age'] = 0  
start_age=18
def age_increment(row):
    global start_age
    row['Age'] = start_age
    start_age+=1
    return row

df = df.apply(lambda filed: age_increment(filed), axis=1)
df.to_csv(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\file1.csv')

df.to_excel(r'C:\Users\jangasa\OneDrive - Republic Services\Desktop\My_Folder\Python\file.xlsx')