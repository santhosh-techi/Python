name=' saNTHosh '
name1='sunny'
print(name.upper())#returns the string in upper case
print(name.lower())#returns the  string in lower case, casefold() performs the same but is is more stronger
print(name.strip())#returns the string by removing the spaces
print(name.title())#starting letter of each word in the sentence as cappital letter
print(name.replace('s','S'))#returns the string y replacing the specific character the provided character
"""returns the string by splitting into substrings if it finds the specific character, 
as we have provided the 'T' as a seperator in it is the part of name, so it split into 'san' and 'Hosh'  in the output"""
print(name.split('T')) # it splits the string into sublists in the form of list
print(name.index('T'))#returns the index of the specific character
print(name1.capitalize())#returns the string by converting the first character of a string as a capital letter
print(name.count('s'))#returns the occurence of a specific character in the given string,syntaxt count('character to find',startpoint,endpoint)
print(name.endswith('o'))#returns boolean value as ouptut if the string ends with the specified value,syntax endswith('character to check',startindex,endindex)
print(name.find('N'))#return the insex value incase it it finds the provided character, else returns -1, similar to index function the only difference is it wont raise exception incase of error
print(name.partition('o')) #returns turple as output contaning 3 items, content before the search element, element and content after search element
"""we have functions like
1.isalpha(): returns boolean value as output id the given string is alphanumeric value i,e a-z and 0-9
2.isascii():returns boolean value as output id the given string is ascii value
3.isnumeric(): returns boolean value as output id the given string value  0-9
4.isdigit(): returns boolean value as output id the given string  value  0-9
5.isdecimal():returns boolean value as output id the given string  value 0-9
"""
print(name.isspace) #returns true if the string contains all the white spaces else false
print(name.istitle())#returns true if all the starting character of each word is capital and remaining are in lower case else returns false)
mylist=['a','b','c','d']
print('_'.join(mylist))#retunrs the string by joining all the iterables
