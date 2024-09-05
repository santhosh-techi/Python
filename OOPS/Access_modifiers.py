class Student:
    def __init__(self,name,rollno,place) -> None:
        self.name=name   #public
        self._rollno=rollno  #private
        self.__place=place  #protected

    def  display1(self): #public method
        print(f'Hi, im {self.name} and my roll no is {self._rollno} and i come from: :{self.__place}')
    
    def  __display2(self): #public method
        print(f'Hi, im {self.name} and my roll no is {self._rollno} and i come from: :{self.__place}')
    
    def  _display3(self): #public method
        print(f'Hi, im {self.name} and my roll no is {self._rollno} and i come from: :{self.__place}')

    def _private_display(self): #private method calling public method
        self.display1()
        self._display3()
        self.__display2()
    
s=Student('santhosh',1,'kamareddy')

s.display1() #public method can access all types of variables of a class
s._Student__display2()  # as the method is protected, we need use name mangling
s._display3() #private method can access all types of variables of a class
s._private_display()