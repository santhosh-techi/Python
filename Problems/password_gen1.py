import random as r
import string as s

def password_generator(size,alpha=s.ascii_letters,digits=s.digits):
    combination=alpha+digits
    password=''.join(r.choice(combination) for value in range(size))
    return password

print(password_generator(10))