#JH's coffe machine project
from random import choice

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}.")
            is_enough= False
    return is_enough

def process_coins():
    print("please insert coins.")
    total=int(input("How many quarters?."))*0.25
    total += int(input("How many dimes?.")) * 0.1
    total += int(input("How many nickles?.")) * 0.05
    total += int(input("How many pennies?.")) * 0.01
    return total


def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False

def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕🍵")




id_on=True

while True:
    choice=input("what would you like?(espresso/latte/cappuccino")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment= process_coins()
           if is_transaction_successful(payment,drink["cost"]):
               make_coffe(choice,drink["ingredients"])







