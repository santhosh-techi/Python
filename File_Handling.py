"""
To deal with Files, we have 3 operations namely, open, read,write 
Open(): is used to open the file, and the pointer will be pointed at the starting location, and it takes 6 modes
Modes:  
    x: it is used to create a new file
    r: reading the file
    w: to write in the file, if data exists, it over rides the file. if not exists create a new file
    a: it is used to append to the existing data content file, starts wrting from the end location,
       as the File Pointer will the at the end of the content
    r+: it is used for read and write the file, it we use write() first, it will start overriding the data instead of erasing the file
    w+: used to read and write, if file doesnt exists it will create a new one
    a+: append and read

read(): it is used to read the content of the file
write(): it is used to write the content in the file
"""
# Try to create a new file and write to it
try:
    with open('test_file.txt', 'x') as file_creation:
        file_creation.write('My name is santhosh')
except FileExistsError:
    print("File already exists.")

# Open the file and read its contents
with open('test_file.txt', 'r') as file_content:
    print(file_content.read())

#to delete the file, we cant delete it directly, inorder to achive this we need to import os
import os
os.remove('file_name') #to remove the file

#to avoid getting error
if os.path.exists('file_name'): #checks the existance of the file
    os.remove('file_name') 
else: print('file name not existed')

#to remove the directory
import os
os.rmdir("myfolder")

#some examples
import os 
with open('file.txt','a+') as file_append:
     print(file_append.write(' name is sunny'))

with open('file.txt','r') as read_file:
     print(read_file.read())
    
if os.path.exists('file.txt'):
     os.remove('file.txt')
    




