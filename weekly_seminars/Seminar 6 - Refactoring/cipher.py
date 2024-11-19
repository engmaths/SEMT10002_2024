import sys
import random

def main():

    action = ""
    while action not in ["encrypt", "decrypt"]:
        action = input("Please enter an action- either encrypt or decrypt")

    shift = ""
    while not shift.isdigit():
        shift = input("Please enter an amount to shift by")
    shift = int(shift)

    input_text = input("Please enter text to process")

    if action == "encrypt":
        encrypted_text = ""
        for char in input_text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        result = encrypted_text

    elif action == "decrypt":
        decrypted_text = ""
        for char in input_text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        result = decrypted_text

    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        sys.exit(1)

    print("Result:", result)

main()
