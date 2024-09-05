l=['sunny','bunny',['santhosh','sreeja','jangam'],'nandappa','saroja']

for i in l:
    if type(i) is not list:
        print(i,end='-')
    else:
        for names in i:
            print(names,end='-')