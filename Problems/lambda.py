"""
1. lambda function is an anonymous function which takes n number of arguements and contains a sngle expression, which will be like an
shortcut of creating a function with multiple lines.
2. lambda function is created by using a keyword called Lambda.
3. lambda function need to be written in a single line
4. Syntax: lambda arguement: expression
5. simply we can say it is a function without name
"""
#Example: for sqauring the each number

def my_function(function,iterable):
    result=[]
    for item in iterable:
        answer=function(item)
        result.append(answer)
    return result

iterable=[1,2,3,4,5]

print(my_function(lambda sqaures:sqaures**2,iterable))

#Example2:
fun=lambda a: True if a>=18 else False
def age_catergory(num):
    age=fun(num)
    print(age)

age_catergory(11)
    