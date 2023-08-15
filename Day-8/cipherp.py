# Ceaser Cipher - Encryption

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q' , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q' , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(plain_text, shift_amount):
    ciphertext = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        ciphertext += new_letter
    print(f'The encoded text is {ciphertext}')    

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        old_position = position - shift_amount
        old_letter = alphabet[old_position]
        plain_text += old_letter
    print(f'The decoded text is {plain_text}')



again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input('Type your message \n').lower()
    shift = int(input('Type the shift number \n'))

    if direction == 'encode':
        encrypt(plain_text= text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(cipher_text=text, shift_amount=shift)
    
    decision = input('Do you want to continue? (Y/N)\n').lower()
    if decision == 'y':
        again = True
    if decision == 'n':
        again = False