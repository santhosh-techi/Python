class Person:
    def __init__(self, fname, lname) -> None:
        self.First_Name = fname
        self.Last_Name = lname
    
    def print_details(self):
        return f'My name is {self.First_Name} {self.Last_Name}'
    
    def __str__(self) -> str:
        return f'My first name is: {self.First_Name} and last name is: {self.Last_Name}'

# Creating a Student class inheriting from Person
class Student(Person):
    def __init__(self, fname, lname, work) -> None:
        super().__init__(fname, lname)
        self.work = work
    def __str__(self) -> str:
        return f'{super().__str__()} and im a { self.work}'
    
    def print_details(self):
        return f'{super().print_details()} and im a {self.work}'
    
# Create an instance of Student
Student1 = Student('Santhosh', 'Kumar', 'Software Engineer')
print(Student1.print_details())
