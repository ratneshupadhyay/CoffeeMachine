from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
menu.menu.append(MenuItem("black coffee", 10,0,15,1))
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True


while machine_on:


    order=input("What Would You Like To Order? ")
    if order == "off":
        print(f" Resources left are: {coffee_maker.resources}")
        machine_on = False
        break


    final = menu.find_drink(order)
    if coffee_maker.is_resource_sufficient(final):

        payment_done = money_machine.make_payment(final.cost)
        if payment_done:

            coffee_maker.make_coffee(final)
    else:
        print("Sorry Cant Process")
check_profit = input(("Do You Want to check profit? type 'Yes' or 'No' ")).lower()
if check_profit == "yes":
    print(f"The Profit is {money_machine.profit}")

