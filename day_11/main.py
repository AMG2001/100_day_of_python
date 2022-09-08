# if your cards more than 21 you loose immediatly
# if king . Queen and jack is = 10
# Ace can be 1 or 11
import random

userCards=[]
computerCards=[]
ace =1
listOfNumbers=[ace,2,3,4,5,6,7,8,9,10,10,10,10]
def get_new_card():
    return random.randint(listOfNumbers[0], listOfNumbers[len(listOfNumbers)-1])
def determine_Ace(total_cards):
    if(total_cards+11<=21):
        return 11
    else:
        return 1
user_flag=True
computer_flag=True
userCards.append(get_new_card())
computerCards.append(get_new_card())
print(f'user first card ->{userCards}')
print(f'Computer Cards -> {computerCards}')
while(user_flag==True or computer_flag==True):
    answer=input("do you want to take new card ??")
    if(answer=='t' or answer =="T"):
        userCards.append(get_new_card())