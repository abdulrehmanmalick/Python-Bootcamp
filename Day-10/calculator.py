import os

def welcomeMsg():
    print('Welcome to Pythonista')

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def OperationChoice():
    print('+')
    print('-')
    print('*')
    print('/')

def operations(a, b, optchoice):
    if optchoice == '+':
        return addition(a,b)
    if optchoice == '-':
        return subtraction(a,b)
    if optchoice == '*':
        return multiplication(a,b)
    if optchoice == '/':
        return division(a,b)

def printfunc(a,optchoice,b):
    print(f'{a} {optchoice} {b}')

def optchoice():
    return input('Pick an operation: ')

def pickNumA():
    return float(input("What's the first number?: "))

def pickNumB():
    return float(input("What's the other number?: "))

doAgain = True

welcomeMsg()


a = pickNumA()
OperationChoice()
optchoices = optchoice()
b = pickNumB()
printfunc(a,optchoices,b)

calculated_value = operations(a, b, optchoices)

while doAgain:
    choice = input(f"Type 'y' to continue calculating with {calculated_value}, or type 'n' to start a new calculation: ").lower()
    if choice == 'n':
        print(f'Final Result: {calculated_value}')
        doAgain = False
    else:
        os.system('cls')
        new_value = calculated_value
        a = new_value
        optchoices = optchoice()
        b = pickNumB()
        print(f'{a} {optchoices} {b}')

        calculated_value = operations(a,b,optchoices)
