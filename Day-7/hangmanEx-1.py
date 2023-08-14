import random

word_list = [
    'ardvark', 'baboon', 'kaboom'
]

# for words in word_list:
#     chosen_word = random.choice(word_list)
chosen_word = random.choice(word_list)

guess = input('Guess a letter?\n').lower()

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')