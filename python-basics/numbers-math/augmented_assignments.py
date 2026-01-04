# Augmented Assignments

# This makes a binary operation
# in one step without needing a
# lot of redundancy

print('\n--- Augmented Assignments ---\n')

print('Way of work:\nvariable <operator>(without the space)= value\n')

# Operations
print('\n--- Operations ---\n')

# Addition

var = 10
var += 5

print(f'Addition\nvar = 10\nvar += 5\nResult: {var}\n')

# Substraction

count = 14
count -= 3

print(f'Substraction\ncount = 14\ncount -= 3\nResult: {count}\n')

# Product

product = 65
product *= 7

print(f'Product\nproduct = 65\nproduct *= 7\nResult: {product}\n')

# Division

price = 100
price /= 4

print(f'Division\nprice = 100\nproduct /= 4\nResult: {price}\n')

# Floor division

total_pages = 23
total_pages //= 5

print(f'Floor Division\ntotal_pages = 23\ntotal_pages //= 5\nResult: {total_pages}\n')

# Modulus

bits = 35
bits %= 2

print(f'Modulus\nbits = 35\nbits %= 2\nResult: {bits}\n')

# Exponentiation

power = 2
power **= 3

print(f'Exponentiation\npower = 2\npower **= 3\nResult: {power}\n')

# With Strings
print('\n--- With Strings ---\n')
print('Only works the one that add up\nlike + or *')

greet = 'Hello'
greet += ' World'

print(f'Concatenate strings\ngreet = \'Hello\'\ngreet += \' World\'\nResult: {greet}\n')

print('To repeat strings use *')

greet = 'Hello'
greet *= 3

print(f'Repeat strings\ngreet = \'Hello\'\ngreet *= 3\nResult: {greet}\n')

print('Substraction and division\ndon\'t work with strings\n')

print('Also ++ and -- do not work on python')
