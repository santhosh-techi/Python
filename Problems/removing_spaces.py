import string as s

def remove_spaces(input_string):
    initial_count=len(input_string)

    new_string=''.join(value for value in input_string if not value.isspace())
    new_string_count=len(new_string)

    print(f'the orginal string is: {input_string} and the lenght is {initial_count}\n and modified string is {new_string} and the count is {new_string_count}')
    

remove_spaces('a b c')