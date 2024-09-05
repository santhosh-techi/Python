Addition=lambda x,y:x+y
Subtraction=lambda x,y:x-y
Multiplication=lambda x,y:x*y
Division=lambda x,y: round(x//y)
Modulus=lambda x,y:round(x%y)

operation_dict={
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '//': Division,
    '%': Modulus  }

def Operation():
    #getting the fist number from the user
    num1=int(input('enter first number: '))
    #printing the available operations
    Flag=True
    while Flag:
        for operations in operation_dict:  print(operations)
        #take the operations to be performed
        operation=input('choose the operation: ')
        #getting the Second number from the user
        num2=int(input('enter Second number: '))
        #getting the value of respective operation key
        operation_func=operation_dict.get(operation)
        symbols_list=[symbol for symbol in operation_dict.values()]
        if operation_func in symbols_list:
            result=operation_func(num1,num2)
        else:
            raise 'invalid Operational Symbol'
        
        print(f'the result for the operation choosen is {result}')

        Occurance_operation=input('Enter "Y" to start the operation again, "N" to exit and "O" to start the new Operation : ').lower()
        if Occurance_operation =='y' :
            num1=result
        elif Occurance_operation=='o':
            Operation()
        elif Occurance_operation=='n':
            Flag=False
            print('Bye for the day')

Operation()



