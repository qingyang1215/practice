"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""


def case_counter():
    text = input ("Write down the sentence here: ")
    uppercase_count = 0
    lowercase_count = 0

    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
    
    print(f"Uppercase letters: {uppercase_count}\nLowercase letters: {lowercase_count}" )

case_counter()

# Test cases
# print(case_counter("Hello World!"))  # Expected: Uppercase letters: 2, Lowercase letters: 8
# print(case_counter("PYTHON"))  # Expected: Uppercase letters: 6, Lowercase letters: 0
# print(case_counter("python"))  # Expected: Uppercase letters: 0, Lowercase letters: 6
# print(case_counter("1234!@#$"))  # Expected: Uppercase letters: 0, Lowercase letters: 0
