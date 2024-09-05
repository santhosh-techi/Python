no_of_lines=9
for i in range(no_of_lines):
    for j in range(no_of_lines):
        if (i==0 or i==no_of_lines-1 or i==(no_of_lines//2)):
            print('*',end='')
        elif(j==0 and i<=(no_of_lines//2)):
            print('*',end='')
        elif(j==no_of_lines-1 and i>(no_of_lines//2) and i!=no_of_lines-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
