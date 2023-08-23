# BlackJack is a game played using cards
# Goal of the game is to add the cards to the largest number without going over 21. If the Cards added together and their value go above 21 it is called a BUST and it means you lose immediately
# J-Q-K -> Counted as 10
# cards 2 to 10 -> Face value
# Ace -> 1 it can be either counted as 11 or 1. If ur total is going over 21 then u can count it as 1. else u can count it as 11
############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os


def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'Lose, opponent has blackjack'
    elif user_score == 0:
        return 'Win with a blackjack'
    elif user_score > 21:
        return 'You went over, you lose'
    elif computer_score > 21:
        return 'Opponent went over. You win!'
    elif user_score > computer_score:
        return 'You Win!'
    else:
        return 'You Lose'
    

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' Your Cards: {user_cards}, currennt score: {user_score}')
        print(f" Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))




while input('Do you want to play BlackJack? (Y/N) ').lower() == 'y':
    os.system('cls')
    play_game()
