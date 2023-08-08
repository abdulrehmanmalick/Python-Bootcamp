# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



randNames = len(names)

randName = random.randint(0, randNames -1)
personPaying = names[randName]

print(f'{personPaying} is going to buy the meal today!')