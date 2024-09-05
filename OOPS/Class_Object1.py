class Animal:
    Class_type='Animal Class'
    def __init__(self,name,type) -> None:
        self.name=name
        self.type=type
    
    def __str__(self):
        return f'{self.name} and it is {self.type}'
    
    @classmethod
    def _getclass_details(cls):
        print(cls.Class_type)

    @staticmethod
    def _get_info():
        return 'This is a Animal Class'
    
    def _get_making_sound(self,sound):
        return f'{self.name} and it can make sound {sound}'
    
Dog=Animal('Dog','Carnivorous')
Monkey=Animal('Monkey','Herbivorous')

print(Dog)
print(Monkey)
print(Dog._get_making_sound(True))
print(Dog._get_info())