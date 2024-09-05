"""Nonlocal keyword is used inside the nested function and if we use a nonlocal keyword it will work with the 
variables which are declared above the nested function
"""
def func1():
    x='im local1'
    def fun2():
        nonlocal x
        x='im a local2'
        print(x)
    fun2()
    print(x)

func1()
