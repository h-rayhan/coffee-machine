from menu import MENU

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash": 10
}


def display_resources():
    print(f"Water: {RESOURCES["water"]} ml\nMilk: {RESOURCES["milk"]} ml\nCoffee: {RESOURCES["coffee"]} g"
          f"\nCash: ${RESOURCES["cash"]}")


def top_up():
    """Turns off the coffee machine to top up."""
    print("The coffee machine has been turned off.")
    input("Top up water tank. Press enter to confirm\n")
    RESOURCES["water"] = 300

    input("Top up milk tank. Press enter to confirm\n")
    RESOURCES["milk"] = 200

    input("Top up coffee grounds. Press enter to confirm\n")
    RESOURCES["coffee"] = 100


def check_coffee_cost(quarters, dimes, nickels, pennies, coffee):
    """Checks if the customer has entered enough money for the coffee."""
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    coffee_cost = MENU[coffee]["cost"]

    if total >= coffee_cost:
        change = total - MENU[coffee]['cost']
        RESOURCES["cash"] += coffee_cost
        print(f"\nHere is your change: ${change}")
        return True
    else:
        return False
