import random

word_list = ['ardvark', 'baboon', 'kaboom']
display = []

for words in word_list:
    chosen_word = random.choice(word_list)

print(f'Chosen Word is {chosen_word}')

for _ in range(len(chosen_word)):
    display.append('_')
print(display)


guess = input('Guess a letter?\n').lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
       
print(display)


