"""Python doesn't support Abstract class and methods by default
But inorder to acheive this, we need to import ABC(Abstraction base classes), Abstractionmethod from the abc module
And in python, we cant create an Object for the Abstraction class
Below is the example for the same
An Abstract class might contain one or more abstract methods along with normal methods,so we call those kind of class as Concrete class"""

from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    #defining abstraction method: method only with defination is called abstract methods
    def work(self):
        pass

#creating an object for abstract computer class
#c=computer()
""" And the error msg is   c=computer() TypeError: Can't instantiate abstract class computer with abstract method work"""

"""So to achive this, we need to  inherit the parent class and override the parent method
even after inheriting the abstract parent class and not overriding the abstract methods, still we cant create the object for child class
as well"""

#class laptop(computer):
  #  pass

#l=laptop()
'''Error msg is :    
 l=laptop()
TypeError: Can't instantiate abstract class laptop with abstract method work'''

'''So we need to overide all thw abstract methods of abstract class'''
class laptop:
    def work(self):
        print('im working')
    
l=laptop()
l.work()

"""if a class contains complete abstract methods then its a interface, similar to the abstract class, we cannot create instances
for the interface class, so similar to abstraction, we need to override all the interface methods in the child class
Below is the example as show"""

class interface(ABC):
    @abstractmethod
    def working(self):
        pass
    def walking(self):
        pass
    def sitting(self):
        pass
  
#i=interface() #Error:cant instantiate the abstrace class

class inter(interface):
    def working(self):
        print('i ll print')
      
    def walking(self):
        print('i ll walk')
      
    def sitting(self):
        print('im sitting')

i=inter()
i.sitting()

"""Even if we define the constructor in the abstract class, we cant instantiate the class,
below is the example for the same.
"""
from abc import ABC,abstractmethod

class water_boiler(ABC):
    def __init__(self) -> None:
        print('im a boiling water class')
      
    @abstractmethod
    def boiling_method(self):
        pass


C=water_boiler()
print(C)
      
