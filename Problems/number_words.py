def number_to_text(number):
    num=number

    if num==0:
        return 'zero'

    below_20=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
           'fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    thousands=['','hundred','thousand','Lakh']

    if num==1:
        return below_20[num]
    elif num<20 :
       return below_20[num]
    elif num>=20 and num<100:
        return tens[num//10]+' '+below_20[num%10]
    elif num>=100 and num<1000:
        return below_20[num//100] +' '+thousands[1]+' '+'' if number_to_text(num%100)=='zero' else number_to_text(num%100) 
    elif num>=1000 and num<=10000:
        return below_20[num//1000]+' '+thousands[2]+' '+'' if number_to_text(num%1000)=='zero' else number_to_text(num%1000) 
    else:
        return 'number is greater then one 10 thousand'
    

print(number_to_text(100))
        

        



    
