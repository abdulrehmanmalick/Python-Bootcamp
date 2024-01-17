import random as rd
import os
import time

easyGuess = 10
hardGuess = 5


def welcome():
    print("Welcome to the Number Guessing Game! \n")

def randGuess():
    num = rd.randint(1,100)
    print("I am thinking of a number between 1 to 100")
    return num

def difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return choice

def playagain():
    playAgain = input('Do you want to play again? (Y/N) \n')
    if playAgain == 'Y':
        os.system('clear')
        main()
    else:
        os.system('clear')
        print('Thank you for playing! \n')
        exit()
  
def main():
    welcome()
    secret_num = randGuess()
    time.sleep(1)
    os.system('clear')
    user_choice = difficulty()

    if user_choice == 'easy':
        print(f'You have {easyGuess} guesses \n')
        tries = 10
        while tries != 0:
            userNum = int(input('Enter a number between 1 to 100: '))
            if userNum != secret_num:
                if userNum > secret_num:
                    print('Try a lower number \n')
                elif userNum < secret_num:
                    print('Try a higher number \n')
                
                        
                tries -= 1
                
            elif userNum == secret_num:
                print(f'You guess it right, the Secret Number was: {secret_num}, your guess: {userNum}')
                playagain()
        
        print('You ran out of tries, better luck next time \n')
        playagain()
                

    elif user_choice == 'hard':
        print(f'You have {hardGuess} guesses \n')
        tries = 5
        while tries != 0:
            userNum = int(input('Enter a number between 1 to 100: '))
            if userNum != secret_num:
                if userNum > secret_num:
                    print('Try a lower number \n')
                elif userNum < secret_num:
                    print('Try a higher number \n')
                
                        
                tries -= 1
                
            elif userNum == secret_num:
                print(f'You guess it right, the Secret Number was: {secret_num}, your guess: {userNum}')
                playagain()
        
        print('You ran out of tries, better luck next time \n')
        playagain()


if __name__ == "__main__":
    main()



