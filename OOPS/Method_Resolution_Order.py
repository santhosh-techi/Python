"""In python, we can achive the multiple inheritance using MRO: Method Resolution Order
If the class contains same properties or behavior which is being inherited to sub-class, properties/methods will be called
from left to roght order"""

class Student():
    def __init__(self,name,age,address) -> None:
        self.Student_name=name
        self.Student_age=age
        self.Student_address=address
    
    def __str__(self) -> str:
        return f'I belong to Student class'
    
    def __get_student_details(self):
        print(f'Student_name :{self.Student_name}')
        print(f'Student_age :{self.Student_age}')
        print(f'Student_Address :{self.Student_address}')
    
class School():
    def __init__(self,Obj_name,sch_name,roll_no,student_std,student_section,address) -> None:
        self.Student_name=Obj_name.Student_name
        self.school_name=sch_name
        self.Student_roll_no=roll_no
        self.Student_Std=student_std
        self.Student_section=student_section
        self.School_address=address
    
    def __str__(self) -> str:
        return f'I belong to School class'
    
    def _get_school_details(self,Obj):
        print(f'School_name :{self.school_name}')
        print(f'Student_name :{Obj.Student_name}')
        print(f'Student_Roll_No :{self.Student_roll_no}')
        print(f'Student_Std :{self.Student_Std}')
        print(f'Student_section :{self.Student_section}')
        print(f'Student_School_Address :{self.School_address}')
    
class user(Student,School):
    def __init__(self, name, age, address) -> None:
        super().__init__(name, age, address)

std1=user('santhosh',26,'Kamareddy')
sch1=School(std1,'KTS','kamareddy','Fourth-Class','A','Kamareddy')
sch1._get_school_details(std1)



