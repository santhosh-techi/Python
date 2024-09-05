
def _sqaure_of_integers(number):
    #checking the given number is even or odd number
    if number%2==0:
        mid=number//2
    else:
        mid=(number//2) +1
    
    #declaring the value to store the square of 2 integers
    sum_of_squares=0
    list=[]
    for i in range(mid+1):
        for j in range(mid+1):
            sum_of_squares=i*i + j*j
            if sum_of_squares==number:
                return (i,j)
                break
    else:
        return 0    
print(_sqaure_of_integers(26))


    


    








