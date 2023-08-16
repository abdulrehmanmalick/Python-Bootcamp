# Dictionary and Nesting
"""
Syntax for dicitonary
{Key: Value}
"""

programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.', 
    'Function' : 'A piece of code that you can easily call over and over again'
}

print(programming_dictionary['Bug'])

# Adding new items to dictionary
programming_dictionary['Loop'] = 'The action of doing something over and over'

print(programming_dictionary)

# We can also create empty dictionary
empty_dictionary = {}

# Edit an idem in dicitonary
programming_dictionary['Bug'] = 'Hello'

print(programming_dictionary)

# loop thorugh a dictionary
for thing in programming_dictionary:
    print(thing) #Just prints the keys
    print(programming_dictionary[thing])

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

