child1={
    "Name":"Sunny",
    "vehiles_list":"car"
}
child2={
    "Name":"Sunny",
    "vehiles_list":["car","bike","cycle"]
}
family_details={
    "child1":child1,
    "child2":child2
}

for child in family_details.keys():
    list=[]
    if child=="child2":
        for key,value in child2.items():
               if key=='vehiles_list':
                    for val in value:
                         list.append(val)
                        

print(list)
                
