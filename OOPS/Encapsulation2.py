class BankAccount:
    def __init__(self,number,bal=0):
        self.__Account_Number=number
        self.__Bank_balance=bal

    def __get_Bankaccount(self):
        print(self.__Account_Number)

    def __get_Bank__balance(self): 
        try:
            if self.__Bank_balance > 0:
                print(f'Your Bank balance is: {self.__Bank_balance}')
            else:
                raise ValueError('Balance cannot be negative or zero')
        except ValueError as e:
            print(f'Error: {e}')
            # Optionally, raise the exception further if needed:
            raise
        else:
            print(f'bank balance is {self.__Bank_balance}')
            print(f'Bank balance is: {self.__Bank_balance}')  #else block will get execute irrespective of condition

    def setting_balance(self,balance):
        self.__Bank_balance+=balance

b=BankAccount('ABCD',28)
print(b._BankAccount__Bank_balance)##printing the balance using name mangling

b.setting_balance(1000)
b._BankAccount__get_Bank__balance()







    

                  