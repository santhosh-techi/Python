import random as r
stage=['''
    |
    0
  ''|''
   / \  
''',
'''  
    |
    0
  ''|''
   /   
''',
'''
    |
    0
  ''|''
''','''
    |
    0
  ''|''
''',
'''
    |
''']
numbers=[0,1,2,3,4,5,6,7,8,9]
try:
    user_value = r.choice(numbers)
    if user_value < 0 or user_value >= len(stage):
        raise IndexError('Value is out of range for stages.')
    
    # If the input is valid and within the range, access the stage
    print(f'Selected stage: {stage[user_value]}')

except ValueError:
    print('User input should be an integer.')
except IndexError as e:
    print(e)
    
