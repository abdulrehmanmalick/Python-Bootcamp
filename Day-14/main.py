# Higher or Lower Game
from game_data import data
import random
from art import logo, vs
import os
import time

def get_random_data():
    return random.choice(data)

def display(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def play_game():
    x = True
    score = 0
    followingscore = True
    choiceA = get_random_data()
    choiceB = get_random_data()

    if choiceA == choiceB:
        choiceB = get_random_data()

    while x:
        print("A:", display(choiceA))
        print('\n')
        print("B:", display(choiceB))

        followerCountA = choiceA["follower_count"]
        followerCountB = choiceB["follower_count"]

        if followerCountA > followerCountB:
            followingscore = True
        else:
            followingscore = False

        user_choice = input('Who has more followers on Insta? (A or B?) \n').lower()

        if followingscore and user_choice == 'a':
            print('Correct! A has more followers.')
            score += 1
        elif not followingscore and user_choice == 'b':
            print('Correct! B has more followers.')
            score += 1
        else:
            print(f'Wrong guess. Your final score: {score}')
            x = False

        choiceA = choiceB
        choiceB = get_random_data()

        print(f"Your current score: {score}\n")

    return score

def main():
    print(logo)
    print("Welcome to the game!! \n")
    time.sleep(1)
    os.system('clear')

    play_again = True
    while play_again:
        final_score = play_game()
        play_again_input = input(f"Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again_input != 'yes':
            play_again = False
        os.system('clear') 

    print(f"Thanks for playing! Your highest score was: {final_score}")

if __name__ == "__main__":
    main()
