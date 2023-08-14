# Simple Function
def greet():
    print('Hello')
    print('I am learning coding')
    print('Python looks fun')

greet()

# Function that allows for input
def greeting(name):
    print(f'Hello {name}')
    print(f'How do you do {name}?')
    print(f'Is {name} your name?')
greeting('abd')

def addition(x,y):
    sum = x + y
    print(sum)
addition(1,3) 

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'Hey {name}! Should we meet at {location}?')
greet_with('Abdul Rehman', 'Chaivinist')

def multplication(a,b,c):
    product = a * b * c
    print(product)

multplication(5,3,2)


def multplication(c=2, b=1, a=4):
    product = a * b * c
    print(product)

multplication()