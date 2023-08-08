# Rock Paper Scissor
import random

choiceList = ['Rock', 'Paper', 'Scissor']


# choice = input('Rock Paper or Scissor? \n')

randChoice = len(choiceList)

random_choice = random.randint(0, randChoice - 1)
choice = choiceList[random_choice]


