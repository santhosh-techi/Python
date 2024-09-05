class Animal:
    def __init__(self,name,type) -> None:
        self.name=name
        self.type=type

    @classmethod
    def method(cls, name, type):
        # Create and return an instance of Animal
        return cls(name, type)

# Using the class method to create an instance
#a = Animal.method('dog', 'doggy')
a=Animal.method('dog','Doggy')

# Print the instance's attributes
print(a.name)  # Output: dog
print(a.type)  # Output: doggy

print(a)
