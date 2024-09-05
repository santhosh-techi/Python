#positional Arguements: argumebts ordered is not followed with the defination of paramaters

def greet(name, greeting):
    print(f'Hi good{greeting} !! my name is {name}')

greet('sunny','morning')
greet('morning','sunny')

#Keywork Arguements:to overcome the issue of positional arguements, we follow key and value type
greet(name='sunny',greeting='moring')

#note: Positional arguements to be followed by keyword arguements else it will raise error

#default Arguemebts: giving a default values
def greet1(name='abc', greeting='ABC'):
    print(f'Hi good{greeting} !! my name is {name}')

greet1('suy','xby')

#Arbitary Arguements
#Positional Arbitary Argumenbts
def add(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print(f'sum of numbers ={sum}')

add(1,2,3,4,5)

#Positional Arbitary Arguements:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(lname='sunny',l='santhosh')