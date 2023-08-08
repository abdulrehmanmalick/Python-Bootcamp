# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

name1 = input("Enter first Name \n")
name2 = input("Enter second name Name \n")



lowercase_name1 = name1.lower()
lowercase_name2  = name2.lower()


names = lowercase_name1 + lowercase_name2
print(names)

count_t = names.count('t')
count_r = names.count('r')
count_u = names.count('u')
count_e = names.count('e')


count_true = count_t + count_r + count_u + count_e


count_l = names.count('l')
count_o = names.count('o')
count_v = names.count('v')
count_e = names.count('e')

count_love = count_l + count_o + count_v + count_e

loveScore = str(count_true) + str(count_love) 

loveScore = int(loveScore)


if loveScore < 10 and loveScore >= 90:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore >= 40 and loveScore <= 50:
    print(f'Your score is {loveScore}, you are alright together.')
else:
    print(f'Your score is {loveScore}')


