lines=int(10)


for i in range(lines+1):
    for j in range(lines+1):
        if i==0 or i==lines or i==(lines)//2 or j==0:
            print('E',end=' ')
    print()