#  input-> What would you like? (espresso/latte/cappuccino):
# after completion of every input execution
MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "Cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "Cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "Cost": 3.0,
    }
}
resources = {
    "Water": 3000,
    "Milk": 2000,
    "Coffee": 1000,
    "Money": 0
}

input_coins = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}
refill_res = resources.copy()


def check_requirement(coffeetype):
    # check requirements -> if fulfilled print Here is your coffee_symbol {coffe_name} and update resources values
    # if not print sorry there is not enough {item that is not enough}
    for ing in MENU[coffeetype]["ingredients"]:
        if resources[ing] < MENU[coffeetype]["ingredients"][ing]:
            print(f"sorry there is not enough {ing}")
            return False
    return True


def check_cost(cost, coffeetype):
    # calculate total money inserted and return extra:if insufficient print Sorry thats not enough money. money refunded
    total = 0.00
    total += int(input_coins['quarters']) * 0.50
    total += int(input_coins['dimes']) * 0.10
    total += int(input_coins['nickles']) * 0.05
    total += int(input_coins['pennies']) * 0.01

    if total < cost:
        print(f"Sorry that's not enough money. Money refunded {total}\n")
        return False

    elif total == cost:
        return check_requirement(coffeetype)
    else:
        if check_requirement(coffeetype):
            print(f"Returned money : {total - cost}\n")
            return True
        return False


def update(coffeetype):
    for ingredient in MENU[coffeetype]["ingredients"]:
        resources[ingredient] -= MENU[coffeetype]["ingredients"][ingredient]
    resources["Money"] += MENU[coffeetype]["Cost"]


def check(coffeetype):
    if check_cost(MENU[coffeetype]['Cost'], coffeetype):
        print(f"Here is your '{coffeetype}'\n")
        update(coffeetype)


def report(resource):
    print(f"Water : ${resources['Water']}ml")
    print(f"Coffee : ${resources['Coffee']}g")
    print(f"Milk : {resources['Milk']}ml")
    print(f"Money : ${resources['Money']}")


def refill():
    for items in resources:
        resources[items] = refill_res[items]


machineStatus = "on"
while machineStatus == "on":
    print("""Machine instructions:
    \tTo switch off machine: click 'off 
    \tTo refill machine: click 'refill' 
    \tTo check items in machine: click 'report' 
    \tEnjoy the Coffee!!\n""")

    coffeeType = input(" What would you like? (Espresso/Latte/Cappuccino): ")
    coffeeType = coffeeType.lower()

    # switch off machine when said off
    if coffeeType == 'off':
        machineStatus = coffeeType

    # create function report: which gets invoked if user asks report
    # prints qty. of water milk coffee(g) money
    if coffeeType == 'report':
        report(resources)
        continue

    if coffeeType == 'refill':
        refill()
        continue
    #  when user chooses any one ->  print please insert coins.
    print("\nPlease enter coins ")

    #  inputs -> How many quarters($0.25)?:    How many dimes($0.10)/ nickles($0.05)/pennies($0.01)  ( four questions)
    for key in input_coins:
        coin = input(f"How many {key}?")
        if coin.isdigit() and int(coin) >= 0:
            input_coins[key] = int(coin)
    if coffeeType == 'latte' or coffeeType == 'cappuccino' or coffeeType == 'espresso':
        check(coffeeType)
    else:
        print('Invalid choice! Retry')

    for val in input_coins:
        input_coins[val] = 0
