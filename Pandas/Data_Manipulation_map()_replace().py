import pandas as pd
dataset={
    'First_Name': ['Corey','Jane','John'],
    'Last_Name':['Schafer','Doe','Smith'],
    'Email' :['CoreySchafer@gmail.com','JaneDoe@gmail.com','JohnSmith@gmail.com']
}
#df=pd.DataFrame(dataset)
#map(): it only works on series,and it is used for substituting each value in a series with another value
#print(df['First_Name'].map({'Corey':'CoreY'})) #it effects entire series and other values with be non empty values
#in order to modify only one values then we need to use replace()
#print(df['First_Name'].replace({'Corey':'CoreY'}))

#another examples of map() function is, it is used to replace the values with another dataframe
df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana','Custard_Apple']
})
#print(df)
# Dictionary to map fruit names to their colors
color_map = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Orange': 'Orange'
}
# Use .map() to map the 'Fruit' column to the corresponding color
df['Color'] = df['Fruit'].map(color_map)
print(df)

