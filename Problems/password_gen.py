import random as r

Capitals='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Smalls=Capitals.lower()
Numbers='1234567890'
Special_char='!@#$%^&*()_+-={[]}|\:;"?>,<~`'
len_of_caps=input('How many capital letters you need: ')
len_of_small=int(input('How many small letters you need: '))
len_of_Num=int(input('How many Numbers you need: '))
len_of_Special=int(input('How many Special characters you need: '))

try:
    if type(len_of_caps)!=int or type(len_of_small)!=int or type(len_of_Num)!=int or type(len_of_Special)!=int:
        raise Exception('Unformated values were provided')
    else:
        while True:
            password=''
            #capturing Upper case
            password+=''.join(r.choice(Capitals) for i in range(len_of_caps))
            password+=''.join(r.choice(Smalls) for i in range(len_of_small))
            password+=''.join(r.choice(Numbers) for i in range(len_of_Num))
            password+=''.join(r.choice(Special_char) for i in range(len_of_Special))
            #generate final random values
            password=''.join(r.sample(password,len(password)))
            print(f'Your password is: {password}')
            break
except Exception as e:
    print(e)



