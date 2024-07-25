import time
from menu import MENU
from maintenance import RESOURCES, check_coffee_cost


def check_resources(coffee_selected):
    """Checks if there is enough water, milk or coffee in the coffee machine"""
    water = MENU[coffee_selected]["ingredients"]["water"]
    coffee = MENU[coffee_selected]["ingredients"]["coffee"]

    if coffee_selected != "espresso":
        milk = MENU[coffee_selected]["ingredients"]["milk"]
        if RESOURCES["milk"] < milk or RESOURCES["water"] < water or RESOURCES["coffee"] < coffee:
            return False
        else:
            return True
    elif RESOURCES["water"] < water or RESOURCES["coffee"] < coffee:
        return False
    else:
        return True


def check_coins(coffee):
    """Checks if customer has entered enough coins for the selected coffee"""
    quarter = int(input("How many quarters?\n"))
    dime = int(input("How many dimes?\n"))
    nickel = int(input("How many nickles?\n"))
    penny = int(input("How many pennies?\n"))

    status = check_coffee_cost(quarters=quarter, dimes=dime, nickels=nickel, pennies=penny, coffee=coffee)

    if status is True:
        return True
    else:
        return False


def espresso():
    """Makes delicious espresso"""
    RESOURCES["water"] -= MENU["espresso"]["ingredients"]["water"]
    RESOURCES["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    print("\nEnjoy your Espresso! ☕️")
    time.sleep(5)


def latte():
    """Makes delicious latte"""
    RESOURCES["water"] -= MENU["latte"]["ingredients"]["water"]
    RESOURCES["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    RESOURCES["milk"] -= MENU["latte"]["ingredients"]["milk"]
    print("\nEnjoy your Latte! ☕️")
    time.sleep(5)


def cappuccino():
    """Makes delicious cappuccino"""
    RESOURCES["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    RESOURCES["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    RESOURCES["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    print("\nEnjoy your Cappuccino! ☕️")
    time.sleep(5)
