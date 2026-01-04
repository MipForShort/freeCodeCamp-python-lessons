# String concatenation and interpolation
print('\n--- String concatenation & interpolation ---\n')

# Concat
str_1 = 'Hello'
str_2 = 'World'

str_plus_str = str_1 + ' ' + str_2
print('Correct concat: both variables are strings\nstr_1 + \' \' + str_2')
print(str_plus_str, '\n')

# Wrong concat, in a try... catch cause why not
name = 'John Dow'
age = 26

try:
    print('Wrong form of concat')
    print('print(name + age)\n')
    name_and_age = name + age
    print(name_and_age)
except Exception as e:
    print(f'An exception ocurred: {type(e).__name__}')
    print(f'Error message: {e}\n')

# Right way of concat, every datatype other than str has to be explicitly be a str()
print('Right way with str()')
print('name + str(age)')

name_and_age = name + str(age)
print(name_and_age, '\n')

# Augmented operators
print('Augmented operators')

name_and_age = name
print(f'Only name:\n{name_and_age}\n')
name_and_age += str(age)
print(f'Append:\n{name_and_age}\n')

# F-strings
# Just one example as in the previous code
# those have been used for this notes

print('F-strings')
print("Basic sintax, just use f''\nUse {} for variables or expressions\n")

num_1 = 5
num_2 = 10
print(f'The sum of {num_1} and {num_2} is {num_1 + num_2}')
