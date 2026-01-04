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


