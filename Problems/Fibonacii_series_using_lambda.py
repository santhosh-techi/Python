sum = lambda a,b : a+b

def fibonacii_series(num):
    fibonacii_series_list=[]
    if num==0:
        print(0) 
    elif num==1:
        print(1)
    else:
        a=0
        b=1
        for i in range(2,num+1):
            c=sum(a,b)
            if c<=num:
                fibonacii_series_list.append(c)
            a=b
            b=c
    print(f'The fibonacii series of numbers which is less than {num} is: {fibonacii_series_list}')
    
fibonacii_series(100)
