# think on number between 1 and 100
# user choose level , if level is easy then attempts = 10 .
# if level is hard then attempts = 5 .
# if user enter number larger than random generated number then print too high .
# if user enter number lower than generated number then print to low .

import random as rand

attempts = 0


def generate_random_number():
    randomNumber = rand.randint(1, 100)
    print(randomNumber)
    return randomNumber


def check_complexity():
    global attempts
    userChoice = input("choose complexity level : \" hard \" or \"easy \" ??")
    if (userChoice == "easy"):
        attempts = 10
        print(f'attempts = {attempts}')
        return attempts
    elif (userChoice == "hard"):
        attempts = 5
        print(f'attempts = {attempts}')
        return attempts
    else:
        print("enter right value !!")
        check_complexity()


def validate_user_input():
    global attempts
    global randomNumber
    if (attempts > 0):
        userValue = int(input("Guess the number ?? "))
        if (randomNumber > userValue):
            print("Too low")
            attempts -= 1
            validate_user_input()
        elif(randomNumber < userValue):
            print("Too high")
            attempts -= 1
            validate_user_input()
        else:
            print("you got it ✔✔")
    else:
        print("you finished all your tries 🤦‍😢")


print("welcome in Guess Number game 🤞🤍")
randomNumber = generate_random_number()
attempts = check_complexity()
validate_user_input()
