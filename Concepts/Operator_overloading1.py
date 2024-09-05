import random as r
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def __str__(self):
        return f'Name :{self.name} and the age is {self.age}'
    
    def __gt__(self,other):
        return self.age>other.age

    def __lt__(self,other):
        return self.age<other.age

    def __eq__(self,other):
        names=[self.name,other.name]
        return f'{r.choice(names)} will pay the bill'

p1=Person('santhosh',29)
p2=Person('sunny',29)

if p1>p2:
    print(f'{p1.name} will pay the bill')
elif p1<p2:
    print(f'{p2.name} will pay the bill')
elif p1==p2:
    print(f'{p1==p2}')



