class Animal:
    def __init__(self) -> None:
        self.name='Animal Class as a Super Class' 
    
    def __reveal_class_name(self):
        print(self.name)


obj=Animal()
obj._Animal__reveal_class_name() #Name mangling '_'+Name of the class and method Name