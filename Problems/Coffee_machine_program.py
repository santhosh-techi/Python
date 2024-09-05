import Problemss.Menu_resources as mr
import os
import platform
import time as t

#declaring all the variables:
Water=1000
Milk=500
Coffee=500
Profit=0

logo="""
                __                               
__  _  __ ____ |  |   ____  ____   _____   ____  
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >
             \/          \/            \/     \/ 

"""
def clear_screen():
    if platform.system() == "Windows":
        t.sleep(10)
        os.system('cls')
    else:
        t.sleep(10)
        os.system('clear')

item1,item2,item3='Latte','Expresso','Cappuccino'

def amount_calculation(select_item,total_amount):
    global Water,Milk,Coffee,Profit
    
    # Extract ingredients and cost
    ing_water =  mr.Menu[select_item]["ingredians"]["water"]
    ing_milk =  mr.Menu[select_item]["ingredians"]["milk"]
    ing_coffee = mr.Menu[select_item]["ingredians"]["coffee"]
    cost =  mr.Menu[select_item]["cost"]
    
    print(f"Ingredients: Water: {ing_water}ml, Milk: {ing_milk}ml, Coffee: {ing_coffee}g, Cost: {cost} Rs")
    
    if select_item == 'latte':
        if Water >= mr.Menu["latte"]["ingredians"]["water"] and Milk >= mr.Menu["latte"]["ingredians"]["milk"] and Coffee >= mr.Menu["latte"]["ingredians"]["coffee"]:
            cost = mr.Menu["latte"]["cost"]
            if total_amount >= cost:
                Profit += cost
                Water -= mr.Menu["latte"]["ingredians"]["water"]
                Milk -= mr.Menu["latte"]["ingredians"]["milk"]
                Coffee -= mr.Menu["latte"]["ingredians"]["coffee"]
                change = total_amount - cost
                return f'Please collect your change: {change} along with {select_item.capitalize()}'
            else:
                return 'Not enough money inserted.'
        else:
            return f'Sorry for the inconvenience! The resources for {select_item} are insufficient.'
        
    elif select_item == 'expresso':
        print(f"'Ingrediants': 'Water :'{ing_water}, 'Milk :'{ing_milk}, 'Coffee :'{ing_coffee} and 'Cost :'{cost} ")
        if Water >= mr.Menu["expresso"]["ingredians"]["water"] and Coffee >= mr.Menu["expresso"]["ingredians"]["coffee"]:
            cost = mr.Menu["expresso"]["cost"]
            if total_amount >= cost:
                Profit += cost
                Water -= mr.Menu["expresso"]["ingredians"]["water"]
                Coffee -= mr.Menu["expresso"]["ingredians"]["coffee"]
                change = total_amount - cost
                return f'Please collect your change: {change} along with {select_item.capitalize()}'
            else:
                return 'Not enough money inserted.'
        else:
            return f'Sorry for the inconvenience! The resources for {select_item} are insufficient.'
        
    elif select_item == 'cappuccino':
        print(f"'Ingrediants': 'Water :'{ing_water}, 'Milk :'{ing_milk}, 'Coffee :'{ing_coffee} and 'Cost :'{cost} ")
        if Water >= mr.Menu["cappuccino"]["ingredians"]["water"] and Milk >= mr.Menu["cappuccino"]["ingredians"]["milk"] and Coffee >= mr.Menu["cappuccino"]["ingredians"]["coffee"]:
            cost = mr.Menu["cappuccino"]["cost"]
            if total_amount >= cost:
                Profit += cost
                Water -= mr.Menu["cappuccino"]["ingredians"]["water"]
                Milk -= mr.Menu["cappuccino"]["ingredians"]["milk"]
                Coffee -= mr.Menu["cappuccino"]["ingredians"]["coffee"]
                change = total_amount - cost
                return f'Please collect your change: {change} along with {select_item.capitalize()}'
            else:
                return 'Not enough money inserted.'
        else:
            return f'Sorry for the inconvenience! The resources for {select_item} are insufficient.'

    else:
        return 'Invalid selection.'


machine_on=True
while machine_on:
    print(logo)
    #Choosing the Option 
    select_item=input("What wouod you like to have ? (Latte/Expresso/Cappuccino)\nand enter 'Report' for availale item quantity and 'off' for turing off the machine: " ).lower()
    
    #Turnig off the machine
    if select_item=='off':
         machine_on=False
         print('Thanks for choosing our Service, Visit again to taste another product.. ')

    elif select_item=='report':
        print('The available Quantity of items are as follows:\n')
        print(f'Water is: {Water}ml')
        print(f'Milk is: {Milk}ml')
        print(f'Waater is: {Water}ml')
        print(f'Money is {Profit} Rs.')
    
    elif select_item in ('latte', 'expresso', 'cappuccino'):
        print("Please insert coins: ")
        try:
            rup_5_coins = int(input('How many 5 rupee coins? '))
            rup_10_coins = int(input('How many 10 rupee coins? '))
            rup_20_coins = int(input('How many 20 rupee coins? '))
            
            # Calculating the total amount provided
            total_amount = (rup_5_coins * 5) + (rup_10_coins * 10) + (rup_20_coins * 20)
            print(amount_calculation(select_item, total_amount))
        except ValueError:
            print("Invalid input. Please enter numeric values for coins.")
    
    else:
        print(f'You have chosen an invalid option: {select_item}. Please choose the right option.')
    
    #calling clear screen method to clear the screen
    clear_screen()
    
    






