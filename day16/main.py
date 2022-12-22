MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
    "cash":0,
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def printf(var):
    print(f"{var}")

## to get the order of the user and perform it .
def getOrder():
    order = input("What would you like? (espresso/latte/cappuccino):")
    if(order=="off"):
        turn_of()
    elif(order == "espresso" or order == "latte" or order == "cappuccino"):
        is_resources_available(order)
        getOrder()
        return order
    elif(order=="report"):
        print_report()
        getOrder()
    else:
        print("wrong input !! try again")
        getOrder()


def print_report():
    print(f"water : {resources['water']}")
    print(f"milk : {resources['milk']}")
    printf(f"coffee {resources['coffee']}")
    printf(f"cash : {resources['cash']}")


def add_cash_to_machine(cash):
    resources['cash']+=cash
def process_coins(order):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("how many quarters ? "))
    dimes = int(input("how many dimes ? "))
    nickles = int(input("how many nickles ? "))
    pennies = int(input("how many pennies ? "))
    customer_cash = quarters*.25+dimes*.1+nickles*.05+pennies*.01
    printf(f"Customer cash = {customer_cash}")
    if(customer_cash == MENU[f'{order}']['cost']):
        add_cash_to_machine(customer_cash)
    elif(customer_cash>MENU[f'{order}']['cost']):
        print(f"take your extra money : {customer_cash-MENU[f'{order}']['cost']}")
        add_cash_to_machine(MENU[f'{order}']['cost'])
    else:
        print("your cash is lower than required !!")
        process_coins(order)


## check availability of resources :
def is_resources_available(order):
    if(MENU[f'{order}']['ingredients']['water']<=resources['water']
    and MENU[f'{order}']['ingredients']['coffee']<=resources['coffee']
    and MENU[f'{order}']['ingredients']['milk']<=resources['milk'] ):
        process_coins(order)
        print(f"here is your order : {order}")
        resources['water']-=MENU[f'{order}']['ingredients']['water']
        resources['coffee']-=MENU[f'{order}']['ingredients']['coffee']
        resources['milk']-=MENU[f'{order}']['ingredients']['milk']


    else:
        if(MENU[f'{order}']['ingredients']['water']>resources['water']):
            printf("Sorry there is not enough water.")
        elif(MENU[f'{order}']['ingredients']['coffee']>resources['coffee']):
            printf("Sorry there is not enough Coffee.")
        else:
            printf("Sorry there is not enough Milk.")
## turn off the machine .
def turn_of():
    print("machine turned off #")
    exit(0)

getOrder()
