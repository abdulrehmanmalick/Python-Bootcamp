"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

"""

#Logic - 1
# def prime_checker(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True

#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

    
# n = int(input("Check this number: "))

# if prime_checker(number=n):
#     print('This is a prime number \n')
# else:
#     print('Not a Prime Number \n')

#Coding Room Logic:

#Write your code below this line 👇


def prime_checker(number):
    
    if number <= 1:
        print('Not a Prime Number \n')
    elif number <= 3:
        print('It is a Prime Number\n')
    else:
        is_prime = True
        for i in range(3, number):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print("It's a prime number.\n")
    else:
        print("It's not a prime number.\n")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
