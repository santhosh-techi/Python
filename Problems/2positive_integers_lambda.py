import math
squares=lambda num:num**2
def postive_intergers(value):
    mid_value= round(math.sqrt(value))
    for i in range(1,mid_value+1):
        for j in range(i+1,mid_value+1):
            result=squares(i)+squares(j)
            if result==value:
                return i,j
                break
    return 0

squares=lambda num:num**2
print(postive_intergers(10))
        
    