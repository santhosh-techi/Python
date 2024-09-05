try:
    with open('demo.txt','x') as file_creation:
        file_creation.write('my name is santhosh')
except FileExistsError:
    print('file already existed')
    
finally:
    with open('demo.txt','r+') as file_content:
        print(file_content.read())
        #writing the content into the file
        file_content.write(' im appending aftter the last word')
        #moving the pointer to the begining point
        file_content.seek(0)
        #printing the content
        print(file_content.read())



