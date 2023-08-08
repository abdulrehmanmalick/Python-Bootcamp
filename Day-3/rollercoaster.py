

height = int(input("Enter your height \n"))


if height >= 120:
    print('You can ride')


    age = int(input('Enter your age \n'))

    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age > 18:
        bill = 12
    elif age >= 45 and age <= 55:
        bill = 0

    want_photos = input("Do you want photos? (Y/N) \n")

    if want_photos == 'Y':
        bill += 3

    print(f'The total bill is ${bill}')

else:
    print('You can not ride')


