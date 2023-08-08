# Rock Paper Scissor
import random

choiceList = ['Rock', 'Paper', 'Scissor']



randChoice = len(choiceList)

random_choice = random.randint(0, randChoice - 1)
choice = choiceList[random_choice]


print("Computer's Choice", choice)


Humanchoice = input('Rock Paper or Scissor? \n')
print(choice)

if Humanchoice == 'Rock' and choice == 'Rock':
    print('Draw')
elif Humanchoice == 'Rock' and choice == 'Paper':
    print('Computer Wins!')
elif Humanchoice == 'Rock' and choice == 'Scissor':
    print("You Win!")

if Humanchoice == 'Paper' and choice == 'Paper':
    print('Draw')
elif Humanchoice == 'Paper' and choice == 'Scissor':
    print('Computer Wins!')
elif Humanchoice == 'Paper' and choice == 'Rock':
    print("You Win!")

if Humanchoice == 'Scissor' and choice == 'Scissor':
    print('Draw')
elif Humanchoice == 'Scissor' and choice == 'Rock':
    print('Computer Wins!')
elif Humanchoice == 'Scissor' and choice == 'Paper':
    print("You Win!")