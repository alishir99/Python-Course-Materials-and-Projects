MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def choose():
    ask = input("What would you like? (espresso/latte/cappuccino):").lower()
    return ask


def off(choice):
    if choice == 'off':
        return True


def report(water, milk, coffee, money):
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}"


def is_report(option):
    if option == 'report':
        return True


def check_resources(menu):
    for item in menu:
        if menu[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


def coins_process():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def transaction(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            global  profit
            profit += drink_cost
            print(f"Here is ${change} dollars in change.\nEnjoy your {drink_cost}!")
            return True
        else:
            print(f"Enjoy your {drink_cost}!")
            return True


def make_coffe(drink_name, ingredients):
    for item in ingredients:
        resources[item] -=ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

end = False

while not end:
    option = choose()
    if off(option):
        end = True
    elif is_report(option):
        print(report(resources['water'], resources['milk'], resources['coffee'], profit))

    else:
        drink = MENU[option]
        if check_resources(drink['ingredients']):
            coin = coins_process()
            if transaction(coin, drink['cost']):
              make_coffe(option, drink['ingredients'])

