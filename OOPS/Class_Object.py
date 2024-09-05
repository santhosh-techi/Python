class Family:
    Name_of_class='My Family details' ## class variable which can be accessed by using class name or using object reference too
    
    @classmethod  #class method will have class paramter and need to mention decorator as @classmethod mandatorily
    def _get_info(cls):
        return cls.Name_of_class
    
    @staticmethod
    def _get_class_info_(Obj,obj1,obj2):
        Obj._comparision(obj1,obj2)
        return ' This is My Family details and it is in module:main'
    
    def __init__(self,input_name,input_age):
        self.name=input_name
        self.age=input_age

    def __str__(self) -> str:
        return f'{self.name} and {self.age}'

    def _comparision(self,another_object):
        if self.name==another_object.name and self.age==another_object.age:
            return  True
        else:
            return False
      
    def _printing_name(self,greet):
        print(f'Hi {greet}!!.. and my name is {self.name}')

obj1=Family('santhosh Kumar',26)
obj2=Family('sunny',25)
obj1._printing_name('Good Morning')
print(obj1)
print(obj1._comparision(obj2))
print(Family._get_info())
print(obj1._get_info())
print(Family._get_class_info_())
print(obj1._get_class_info_())