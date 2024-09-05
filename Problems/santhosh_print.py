no_of_lines=8
name='SANTHOSH'
for i in range(no_of_lines):
    for j in range(no_of_lines):
        if (i==0 or i==no_of_lines-1 or i==(no_of_lines//2)):
            print(name[j],end='')
        elif(j==0 and i<=(no_of_lines//2)):
            print(name[j],end='')
        elif(j==no_of_lines-1 and i>(no_of_lines//2) and i!=no_of_lines-1):
            print(name[j],end='')
        else:
            print(' ',end='')
    print()
    