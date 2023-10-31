# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:44:43 2023

@author: salun
"""

import random
import string

def generate_password(length):
    # Define the character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity preference
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is within a reasonable range
    if length < 8:
        length = 8
    elif length > 128:
        length = 128

    # Generate a random password using the selected character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")
