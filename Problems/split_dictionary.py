details={
    'Student':{'Name':'Santhosh','Age': 27,'Address':'Kamareddy'}
}
def split_dic(dictionary):
    result = []
    for value in dictionary.values():
        result.append(value)  # Directly append the value
    return result



for values in details.values():
    result=[]
    if type(values) == dict:
        result.append(split_dic(values))
print(result)