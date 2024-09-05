name='santhosh'
letter_list=[]

for i in name:
    letter_list.append(i)

print(letter_list)

input_letter=input('enter the letter')

if input_letter in letter_list:
    index_of_input_leter=name.index(input_letter)
    del letter_list[index_of_input_leter]
    print(letter_list)