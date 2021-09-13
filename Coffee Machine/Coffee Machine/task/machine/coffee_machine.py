water = 0
milk = 0
coffee = 0
cups = 0
money = 0


def add_resources(water_to_add, milk_to_add, coffee_to_add, cups_to_add, money_to_add):
    global water
    global milk
    global coffee
    global cups
    global money
    water += water_to_add
    milk += milk_to_add
    coffee += coffee_to_add
    cups += cups_to_add
    money += money_to_add


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    operation = input()

    def make_coffee(water_needed, milk_needed, coffee_needed, price):
        if water < water_needed:
            print("Sorry, not enough water!")
        elif milk < milk_needed:
            print("Sorry, not enough milk!")
        elif coffee < coffee_needed:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            add_resources(-water_needed, -milk_needed, -coffee_needed, -1, price)
            print("I have enough resources, making you a coffee!")

    ESPRESSO = "1"
    LATTE = "2"
    CAPPUCCINO = "3"

    if operation == ESPRESSO:
        make_coffee(250, 0, 16, 4)
    elif operation == LATTE:
        make_coffee(350, 75, 20, 7)
    elif operation == CAPPUCCINO:
        make_coffee(200, 100, 12, 6)


def fill():
    print("Write how many ml of water do you want to add:")
    water_to_add = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_to_add = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_to_add = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups_to_add = int(input())
    add_resources(water_to_add, milk_to_add, coffee_to_add, cups_to_add, 0)


def take():
    print("I gave you $", money)
    add_resources(0, 0, 0, 0, -money)


def remaining():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print("$" + str(money) + " of money")


def perform_action():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        print()
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            remaining()
        elif action == "exit":
            break
        print()


add_resources(400, 540, 120, 9, 550)
perform_action()
