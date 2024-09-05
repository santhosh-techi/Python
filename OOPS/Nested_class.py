class Animal:
    def __init__(self) -> None:
        print('im parent class')

    def __method_name(self):
        print('im Animal class')

    class Dog:
        def __init__(self) -> None:
            print('im sub class')
    
    def __method_name(self): # if we have same method in the nested class, methods will be over ridden.
        print('im class Dog')
        
a=Animal()
d=Animal.Dog()
a._Animal__method_name()
a._Animal__method_name() # and if we want to access the nexted elements, we need to access with the main class object itself


