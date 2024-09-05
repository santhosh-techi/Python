var='name'
def global_var():
    #global var
    #print(var) #it will take outer value 
    var='changed' #changing
    print(var)#new value

global_var()
