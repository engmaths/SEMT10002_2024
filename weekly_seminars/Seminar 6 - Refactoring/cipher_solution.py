import sys
import random

def wrap_cases(char, shifted):
    '''
    This function checks whether the cipher shift has moved beyond the end of the alphabet,
    ensuring the cipher wraps around appropriately. i.e it makes a shift of 'z' by 1 end up at
    'a' rather than 'A'
    '''
    if char.islower():
        if shifted > ord('z'):
            shifted -= 26
    elif char.isupper():
        if shifted > ord('Z'):
            shifted -= 26

    return shifted  

def encrypt(text, shift):

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            shifted = wrap_cases(char, shifted)
            encrypted_text+=chr(shifted)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def get_input():

    action = ""
    while action not in ["encrypt", "decrypt"]:
        action = input("Please enter an action- either encrypt or decrypt")

    shift = ""
    while not shift.isdigit():
        shift = input("Please enter an amount to shift by")
    shift = int(shift)

    input_text = input("Please enter text to process")

    return (action, shift, input_text)

def main():

    (action, shift, input_text) = get_input()

    if action == "encrypt":
        result = encrypt(input_text, shift)
    elif action == "decrypt":
        result = decrypt(input_text, shift)
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        sys.exit(1)

    print("Result:", result)


if __name__ == "__main__":
    main()
