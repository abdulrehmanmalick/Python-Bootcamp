from caeserExt import alphabet

# Combine encrypt, decrypt functions into a single function called caesar()
# Call the caesar() function, passing over the text, shift and direction values

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f'The {cipher_direction}d text is {end_text}')

try_again = True

while try_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input('Type your message \n').lower()
    shift = int(input('Type the shift number \n'))
    if shift > 26:
        shift = shift % 26
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    decision = input('Do you want to try again?\n').lower()
    if decision == 'y':
         try_again
    if decision == 'n':
         try_again = False
         print('Goodbye!')