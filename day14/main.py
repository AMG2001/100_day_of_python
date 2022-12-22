import random as rand
from art import logo,vs
from game_data import data
# print the logo of the game .
print(logo)
person1={}
person2={}
right_answer=True
length_of_data=len(data)
score=0

def getRandomValue():
  return rand.randint(0,length_of_data)
def initiatePerson1Data(random_value):
  person1['name']=data[random_value]['name']
  person1['follower_count']=data[random_value]['follower_count']
  person1['description']=data[random_value]['description']
  person1['country']=data[random_value]['country']

def initiatePerson2Data(random_value):
  person2['name']=data[random_value]['name']
  person2['follower_count']=data[random_value]['follower_count']
  person2['description']=data[random_value]['description']
  person2['country']=data[random_value]['country']

first_time=True

while(right_answer==True):
  if(first_time==True):
    initiatePerson1Data(getRandomValue())
    initiatePerson2Data(getRandomValue())
  else:
    person1 = person2
    initiatePerson2Data(getRandomValue())
  first_time=False
  print(f"Compare A : {person1['name']} , a {person1['description']} , from {person1['country']}")
  print(vs)
  print(f"Compare B : {person2['name']} , a {person2['description']} , from {person2['country']}")
  print(f"person 1 score : {person1['follower_count']}")
  print(f"person 2 score : {person2['follower_count']}")
  answer = input("Who has more followers ? Type 'A' or 'B' : ")
  if (person1['follower_count'] >= person2['follower_count'] and answer == "A"):
    score += 1
  elif (person1['follower_count'] <= person2['follower_count'] and answer == "B"):
    score += 1
  else:
    print(f"your score is : {score}")
    right_answer = False


