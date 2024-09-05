name='abccba'
reverse_name=''
for i in range(len(name)):
    reverse_name+=name[len(name)-1-i]
if(name==reverse_name):
    print(f'{name} and {reverse_name} are same so it is a palindrome value')
else:
    print(f'{name} and {reverse_name} are not same, so they are not a palindrome value')