import secrets


def _get_hash_key(name='sunny',*values,**keys):
    concate_values = ''
    #looping to fetch the values in the Arbitary Arguements and concatinating with the concate_values
    for value in values:
        concate_values+=concate_values + str(value)
    
    #looping to fetch the values from the Key Arbitary Arguements and concatinating with the concate_values
    for key in keys.items():
        concate_values+=concate_values + str(key)

    #concatinating the final 
    hash_value =  hash(secrets.choice(concate_values+str(name)))
    return - hash_value if hash_value < 0 else hash_value

print(_get_hash_key(1, 'a', 'santhosh', id=1, class_='abc'))