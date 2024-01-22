"""Module providing simple Python code to play with pylint."""

import string

SHIFT: int = 3
choice = input("would you like to encode or decode?")
word = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
encoded = ""
if choice == "encode":
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x : int = LETTERS.index(letter) + SHIFT
            encoded = encoded + LETTERS[x]
if choice == "decode":
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = LETTERS.index(letter) - SHIFT
            encoded = encoded + LETTERS[x]

print(encoded)
