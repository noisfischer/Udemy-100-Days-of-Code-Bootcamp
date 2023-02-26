from menu import MENU
from menu import resources

# Type report or r to see available resources and money gained from customers
def report():
    welcome = 'y'
    while welcome == 'y':
        welcome = input("READY TO ORDER? PRESS 'ENTER': ")
        if welcome == 'report' or welcome == 'r':
            print(f"\nREPORT:\nWater: {total_water}ml\nMilk: {total_milk}ml\nCoffee: {total_coffee}g\nMoney: ${total_money}\n")
            welcome = 'y'
        elif welcome == 'off':
            quit()
        else:
            return


def order():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'espresso' or user_choice == 'cappuccino' or user_choice == 'latte':
        return user_choice
    elif user_choice.count('c') > 0:
        return 'cappuccino'
    elif user_choice.count('r') > 0:
        return 'espresso'
    elif user_choice.count('l') > 0:
        return 'latte'
    elif user_choice == 'off':
        quit()


e_water = MENU['espresso']['ingredients']['water']
e_coffee = MENU['espresso']['ingredients']['coffee']
espresso = [e_water, e_coffee]

l_water = MENU['latte']['ingredients']['water']
l_milk = MENU['latte']['ingredients']['milk']
l_coffee = MENU['latte']['ingredients']['coffee']
latte = [l_water, l_milk, l_coffee]

c_water = MENU['cappuccino']['ingredients']['water']
c_milk = MENU['cappuccino']['ingredients']['milk']
c_coffee = MENU['cappuccino']['ingredients']['coffee']
cappuccino = [c_water, c_milk, c_coffee]

total_water = resources['water']
total_milk = resources['milk']
total_coffee = resources['coffee']

pennies = .01
nickels = .05
dimes = .10
quarters = .25

total_money = 0

next_customer = 'y'
while next_customer == 'y':

    report()

    restart = 'y'
    while restart == 'y':
        restart = 'n'
        choice = order()

        cost = MENU[choice]['cost']

        if choice == 'espresso' or choice.count('s') > 0:
            if total_water >= e_water and total_coffee >= e_coffee:
                print(f"Please insert ${cost}:\n")
            else:
                print("Sorry, there are not enough resources available to make this beverage.\n")
                restart = 'y'
        elif choice == 'latte' or choice.count('l') > 0:
            if total_water >= l_water and total_milk >= l_milk and total_coffee >= l_coffee:
                print(f"Please insert ${cost}:\n")
            else:
                print("Sorry, there are not enough resources available to make this beverage.\n")
                restart = 'y'
        elif choice == 'cappuccino' or choice.count('c') > 0:
            if total_water >= c_water and total_milk >= c_milk and total_coffee >= c_coffee:
                print(f"Please insert ${cost}:\n")
            else:
                print("Sorry, there are not enough resources available to make this beverage.\n")
                restart = 'y'

    num_pennies = float(input("Pennies: "))
    if num_pennies == 'off':
        quit()
    num_nickels = float(input("Nickels: "))
    if num_nickels == 'off':
        quit()
    num_dimes = float(input("Dimes: "))
    if num_dimes == 'off':
        quit()
    num_quarters = float(input("Quarters: "))
    if num_quarters == 'off':
        quit()

    total_inputted = round(
        sum([num_pennies * pennies, num_nickels * nickels, num_dimes * dimes, num_quarters * quarters]), 2)
    refund = round(total_inputted - cost, 2)

    if total_inputted >= cost:
        total_water = total_water - MENU[choice]['ingredients']['water']
        total_milk = total_milk - MENU[choice]['ingredients']['milk']
        total_coffee = total_coffee - MENU[choice]['ingredients']['coffee']
        total_money += cost
        print(f"You entered ${total_inputted}.")
        if total_inputted > cost:
            print(f"You've been refunded ${refund}.")
        print("Your drink is ready! Thank you for your business.\n")
    else:
        print(f"Sorry, you did not submit enough for a {choice}. Money refunded.\n")
