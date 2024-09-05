class Edureka():
    def __init__(self):
        self.course='Python Course'
        self.__tech='Python'
    
    def print_course(self):
        print(f'{self.course} and language is {self.__tech}')
    
obj=Edureka()
print(obj.course)
#print(obj.__tech) #we get error bcz __tech is a private varible now, inorder to access the private members we use name mangling
obj.print_course()

print(obj._Edureka__tech)
print(obj.self__tech)#Error: AttributeError: 'Edureka' object has no attribute 'self__tech'