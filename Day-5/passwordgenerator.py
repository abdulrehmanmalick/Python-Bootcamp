import random


print('Welcome to Password Generator App')

letters = int(input('How many letters would you like in your password? \n'))
symbols = int(input('How many symbols would you like? \n'))
numbers = int(input('How many numbers would you like? \n'))


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q' , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = ['!','@','#','$','%','^','&','*','(',')', '+', '-', '_']
numbers = ['0','1', '2', '3', '4', '5', '6', '7','8', '9']


password_list = []

for letter in letters:
    password_list.append(random.choice(letters))

for symbol in symbols:
    password_list.append(random.choice(symbols))

for number in numbers:
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ''.join(password_list)

print(password)