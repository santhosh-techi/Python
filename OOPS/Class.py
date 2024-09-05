class Myclass:
    Information='My family details',
    'First_Name'
    'Last_name',
    'Surname',
    'Age',
    'Hobbies',
    'Address'

    def __init__(Child,F_name,L_name,S_name):
        Child.First_name=F_name
        Child.Last_name=L_name


Child_Object=Myclass('Santhosh','','Jangam')  #creating a Child object using the class Myclass blueprint
print(Child_Object)
print(Child_Object.First_name)




