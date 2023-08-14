import random
from hangmanext import word_list
from hangmanext import display
from hangmanext import guessed_letters

print('Welcome to Hangman')

for word in word_list:
    chosen_word = random.choice(word_list)

for _ in chosen_word:
    display.append('_') 

word_length = len(chosen_word)

# For Testing 
print(f'The Chosen Word is {chosen_word}')
print(display)

endGame = False
lives = 5

while not endGame:
    guess = input('Enter your character \n').lower()

    print(f'The character you guessed is: {guess}')

    if guess in guessed_letters:
        print('You already have tried guessing this\n')
        lives -= 1
        if lives == 0:
            endGame = True
            print('You Lose.')
    else:
        guessed_letters.append(guess)
     

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  

    if guess not in chosen_word:
        print('You Guessed it Wrong\n')
        lives -= 1
        if lives == 0:
            endGame = True
            print('You Lose.')

    print(f'You have now {lives} lives left \n')

    print(f"{' '.join(display)}")

    if "_" not in display:
        endGame = True
        print("You win.")

