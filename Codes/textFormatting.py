# Replacing the 'a' characters to 'e'
print(input("Give me a text:\n").replace('a', 'e'))
# Make the text uppercase/lowercase
print(input("Give me a text:\n").upper())
# Change the first letter of the words
print(input("Give me a text:\n").title()) #make the first letter in each word upper case
print(input("Give me a text:\n").capitalize()) #upper case the first letter in this sentence
# Returns the length of the text
print(input("Give me a text:\n").__len__())
# Split the text at different characters
print(input("Give me a text:\n").split(' ')) #split at whitespace
print(input("Give me a text:\n").split('a')) #split at letter a
# Count something specific in a string
print(input("Give me a text:\n").count('a'))
#  Find a specific character or word in the text
# Note: Tt returns the index of first occurrence of the substring, or it returns -1, if the substring is not found.
print(input("Give me a text:\n").find('e'))
print(input("Give me a text:\n").find("lamb"))

# Examine the string to see if it starts or ends which a specific character
# If it returns True, then the text starts/ends with that character, if not then it returns False
print(input("Give me a text:\n").startswith('M'))
print(input("Give me a text:\n").endswith('w'))

# Task 10 - You can check if the string is decimal, alphabetic, digit, uppercase or lowercase
print(input("Give me a text:\n").isdecimal())
print(input("Give me a text:\n").isnumeric())
print(input("Give me a text:\n").isalpha())
print(input("Give me a text:\n").isupper())
print(input("Give me a text:\n").islower())

#------------------------------------
""" ---------------
    FORMAT FUNCTION
    ---------------"""
# Convert base-10 decimal integers
# to floating point numeric constants
print("This site is {0:f}% securely {1}!!".
      format(100, "encrypted"))

# To limit the precision
print("My average of this {0} was {1:.2f}%"
      .format("semester", 78.234876))

# For no decimal places
print("My average of this {0} was {1:.0f}%"
      .format("semester", 78.234876))

# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
      .format("binary", 100))

print("The {0} of 100 is {1:o}"
      .format("octal", 100))

""" 
Example:
This site is 100.000000% securely encrypted!!
My average of this semester was 78.23%
My average of this semester was 78%
The binary of 100 is 1100100
The octal of 100 is 144
"""

#------------------------------------

# Signed numbers
print('Output: {0}'.format(42))
print('Output: {:+d}'.format(42))

print('Output: {0}'.format(-42))
print('Output: {: d}'.format(-42))

#------------------------------------

# Padding numbers
print('{:4d}'.format(42))
print('{:01.5f}'.format(3.141592653589793))

#------------------------------------

print("You will face many defeats in life, but never let yourself be defeated.".split(" ").__len__())
# in boolean statement  => return value: True or False
# other situation       => return length

print("Welcome to USA. Usa is awesome, isn't it? Let's go usa.".lower().count("usa"))

