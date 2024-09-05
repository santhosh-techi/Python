from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        pass
        
class dog(Animal):
    def animal_sound(self):
        print('im dog class')
    
a=Animal()
a.animal_sound()


