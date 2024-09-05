class AdditionNumbers:
    # def __init__(self,value) -> None:
    #     self.number=value

    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,other):
        return f' real number is {self.real+other.real}i and imaginay nunber is {self.imaginary+other.imaginary}j'

n1=AdditionNumbers(1,2)
n2=AdditionNumbers(2,1)
print(n1+n2)


class Example:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self): ##it internally calls the str functions
        return f"a: {self.a}, b: {self.b}"

# Usage
obj1 = Example()
obj2 = Example(10)
obj3 = Example(10, 20)

print(obj1)  # a: 0, b: 0
print(obj2)  # a: 10, b: 0
print(obj3)  # a: 10, b: 20
