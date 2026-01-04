# Conditionals and booleans

print('\n--- Conditionals and booleans ---\n')

print('\n--- Comparison operators ---\n')

print('Equal: ==\n Checks if two values are equal\n')
print('Not equal: !=\n Checks if two values are not equal\n')
print('Greater than: >\nChecks if the value on the left\nis greater than the\nvalue on the right\n')
print('Less than: <\nChecks if the value on the left\nis less than the\nvalue on the right\n')
print('Greater than or equal: >=\nChecks if the value on the left\nis greater or equal than the\nvalue on the right\n')
print('Less than or equal: <=\nChecks if the value on the left\nis less or equal than the\nvalue on the right\n')

# Examples
print('Examples:\n')

print(f'(3 > 4)\n{3 > 4}\n')
print(f'(3 < 4)\n{3 < 4}\n')
print(f'(3 == 4)\n{3 == 4}\n')
print(f'(4 == 4)\n{4 == 4}\n')
print(f'(3 != 4)\n{3 != 4}\n')
print(f'(3 >= 4)\n{3 >= 4}\n')
print(f'(3 <= 4)\n{3 <= 4}\n')

# If-elif-else
# Quick explain:
# It is just basic sintax
print('\n--- if-elif-else ---\n')
print('Look at the code to see the simple sintax')
print('No need for complex stuff\n')

print('''
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
\n''')

age = 12

print('Result:')

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

print()
print('Also, you can use the word: pass')
print('It is used for empty statments')
