import random

print("This is a game of Heads and Tails")


random_toss = random.randint(1,2)

if random_toss == 1:
    print('Heads')
else:
    print('Tails')