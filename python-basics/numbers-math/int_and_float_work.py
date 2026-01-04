# How to work with int and float

print('\n--- Integer and floating point numbers ---\n')

# int is a number with no decimal
# points, either positive or 
# negative

int_1 = 56
int_2 = -4

# I'll use fstrings for my prints.
# I don't have python 3.14 on my device
# to use tstrings :'(
print(f'\n--- Integers ---\n{int_1}\n{int_2}')
print(f'Type\n{type(int_1)}\nType\n{type(int_2)}\n')

# Addition

int_1 = 56
int_2 = 12

print(f'Addition\n\t{int_1}\n+\t{int_2}')
print(f'Result: {int_1 + int_2}\n')

# Substraction

int_1 = 56
int_2 = 12

print(f'Substraction\n\t{int_1}\n-\t{int_2}')
print(f'Result: {int_1 - int_2}\n')

# Multiplication

int_1 = 12
int_2 = 4

print(f'Multiplication\n\t{int_1}\n*\t{int_2}')
print(f'Result: {int_1 * int_2}\n')

# Division

int_1 = 56
int_2 = 12

print(f'Division\n\t{int_1}\n/\t{int_2}')
print(f'Result: {int_1 / int_2}\n')

# Floats

float_1 = -12.0
float_2 = 4.9

print(f'\n--- Floats ---\n{float_1}\n{float_2}')
print(f'Type\n{type(float_1)}\nType\n{type(float_1)}\n')

# Addition

float_1 = 5.4
float_2 = 12.0

print(f'Addition\n\t{float_1}\n+\t{float_2}')
print(f'Result: {float_1 + float_2}\n')

# Substraction

float_1 = 5.4
float_2 = 12.0

print(f'Substraction\n\t{float_2}\n-\t{float_1}')
print(f'Result: {float_2 - float_1}\n')

# Multiplication

float_1 = 5.4
float_2 = 12.0

print(f'Multiplication\n\t{float_2}\n*\t{float_1}')
print(f'Result: {float_2 * float_1}\n')

# Division

float_1 = 5.4
float_2 = 12.0

print(f'Division\n\t{float_2}\n/\t{float_1}')
print(f'Result: {float_2 / float_1}\n')

# Adding an int to a float
# This will make de result be a float

int_1 = 56
float_1 = 5.4

print(f'Adding an int to a float\n\t{int_1}\n+\t{float_1}') 
print(f'Result: {int_1 + float_1}\nType: {type(int_1 + float_1)}\n')
print('This is true for all other three operations\n')

# Modulo operator
# This will return the remainder of 
# the division of two numbers
print('--- Modulo ---\n')
print('This returns the remainder of two numbers divided\nwith %')

int_1 = 56
int_2 = 12

float_1 = 5.4
float_2 = 12.0

print(f'Modulo int\n\t{int_1}\n%\t{int_2}')
print(f'Result: {int_1 % int_2}\n')

print(f'Modulo float\n\t{float_2}\n%\t{float_1}')
print(f'Result: {float_2 % float_1}\n')

# Floor division
# This divides two number and
# returns the greastes int
print('\n--- Floor Division ---')
print('This returns the greatest of the\ndivision of two numbers with //')

int_1 = 56
int_2 = 12

float_1 = 5.4
float_2 = 12.0

print(f'Floor division int\n\t{int_1}\n//\t{int_2}')
print(f'Result: {int_1 // int_2}\n')

print(f'Floor division float\n\t{float_1}\n//\t{float_2}')
print(f'Result: {float_2 // float_1}\n')

# Exponentiation
# This raises a number to the
# power of another
print('\n--- Exponentiation ---\n')
print('This raises a number to the power\nof another with **')

int_1 = 56
int_2 = 12

float_1 = 5.4
float_2 = 12.0

print(f'Exponentiation int\n\t{int_1} ** {int_2}')
print(f'Result: {int_1 ** int_2}\n')

print(f'Exponentiation float\n\t{float_1} ** {float_2}')
print(f'Result: {float_1 ** float_2}\n')

# Python allows to convert numbers to certain type
# and also stringsprint('\n--- Int and Float conversion ---\n')

int_1 = 56 
float_1 = 12.92563

print(f'Int to float with float()\n{int_1}\n{type(int_1)}\nFloat\n{float(int_1)}\n{type(float(int_1))}\n')
print(f'Float to int with int()\n{float_1}\n{type(float_1)}\nInt\n{int(float_1)}\n{type(int(float_1))}\n')

str_int = '45'
str_float = '7.8'

print('Now with strings\n')

print(f'Converted int\n\'{str_int}\'\n{int(str_int)}\n{type(int(str_int))}\n')
print(f'Converted float\n\'{str_float}\'\n{float(str_float)}\n{type(float(str_float))}\n')

# Extra methods that we can use
print('\n--- Extra methods ---\n')


# round()
# This rounds a number to the nearest
# integer and returns with no decimals
print('round()')

int_1 = 4.798
int_2 = 4.253

print(f'Int 1:\n{int_1}\nround(int_1)\n{round(int_1)}\n')
print(f'Int 2:\n{int_2}\nround(int_2, 1)\n{round(int_2, 1)}\n')


# abs()
# Returns the absolute value of a number
print('abs()')

num = -15

print(f'Num:\n{num}\nabs(num)\n{abs(num)}\n')

# pow()
# Returns the raise of a number
# to the power of another, or is a 
# modular exponentiation
print('pow()')

print(f'Result 1:\npow(2, 3)\n{pow(2, 3)}\nEquivalent to 2 ** 3\n')
print(f'Result 2:\npow(2, 3, 5)\n{pow(2, 3, 5)}\nEquivalent to (2 ** 3) % 5\n')
