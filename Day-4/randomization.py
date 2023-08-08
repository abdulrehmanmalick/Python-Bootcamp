import random

#Whole Number
random_integer = random.randint(1,100)
print(random_integer) 


# Floating Number - Range is 0 to 1
random_float = random.random()
print(random_float)
# To expand the range we can multiply our random floating number for eg:
random_float = random.random() * 5
print(random_float) #Now this has a range bw 0 to 5
