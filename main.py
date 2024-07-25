import os
from maintenance import top_up, display_resources
from dispense import espresso, latte, cappuccino, check_resources, check_coins


def clear():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print("What would you like to order?")

        select = input("A. Espresso\nB. Latte\nC. Cappuccino\n\n").lower()
        if select not in ["a", "b", "c", "off", "report", "cash"]:
            clear()
            print("Please enter a valid option")
            continue

        elif select == "a":
            resources = check_resources(coffee_selected="espresso")
            if resources is True:
                if check_coins(coffee="espresso") is True:
                    espresso()
                    clear()
                else:
                    input("Sorry, you have insufficient balance.")
                    clear()
                    continue

        elif select == "b":
            resources = check_resources(coffee_selected="latte")
            if resources is True:
                if check_coins(coffee="latte") is True:
                    latte()
                    clear()
                else:
                    input("Sorry, you have insufficient balance.")
                    clear()
                    continue

        elif select == "c":
            resources = check_resources(coffee_selected="cappuccino")
            if resources is True:
                if check_coins(coffee="cappuccino") is True:
                    cappuccino()
                    clear()
                else:
                    input("Sorry, you have insufficient balance.")
                    clear()
                    continue

        # 'report' displays the water, milk and coffee
        elif select == "report":
            clear()
            display_resources()

            # gives the user to turn off the machine to top up
            check = input("\nType 'off' to top up or else press enter to continue\n\n")
            if check == "off":
                clear()
                top_up()

                input("The coffee machine has been topped up. Press enter to turn on coffee machine\n")
                clear()

        else:
            break


main()
