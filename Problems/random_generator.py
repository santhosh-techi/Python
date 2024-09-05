import random as rdm
import time

upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case=upper_case.lower()
numeric_values='1234567890'
alpha_values='!@#$%^&*()_-+}{|}\":?><,'
random_number= upper_case+lower_case+numeric_values+alpha_values
ran_gen=''.join(random_number)
for i in range(10):
    print(''.join(rdm.sample(ran_gen,20)))
    time.sleep(0.2)
    i+=1