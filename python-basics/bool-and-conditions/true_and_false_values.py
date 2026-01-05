# Truthy and Falsy values

print(f'\n--- Truthy and Falsy values ---\n')

print('Values like the next are falsy')
print(f'{None}\n{False}\nInt: {0}\nFloat: {0.0}\nEmpty Strings:  ""\n')

print('Other values like non-zero and\nnon-empty strings are truthy\n')

# You can use bool() to check for
# those values
print('Use bool() to know what a value is')

print(f'bool(False): {bool(False)}')
print(f'bool(0): {bool(0)}')
print(f'bool(\'\'): {bool(False)}')
print()
print(f'bool(True): {bool(True)}')
print(f'bool(1): {bool(1)}')
print(f'bool(\'Hello\'): {bool('Hello')}')

print('\n--- Logical operators ---\n')
print('There are three: and, or, not')

print('Here are the true and false tables for each one\n')

print(f'and:\nTrue and True: {True and True}\nTrue and False: {True and False}\nFalse and True: {False and True}\nFalse and False: {False and False}\n')
print(f'or:\nTrue or True: {True or True}\nTrue or False: {True or False}\nFalse or True: {False or True}\nFalse or False: {False or False}\n')
print(f'not:\nnot True: {not True}\nnot False: {not False}\n')

print('Examples for not')
print(f'not \'\': {not ''}')
print(f'not \'Hello\': {not 'Hello'}')
print(f'not 0: {not 0}')
print(f'not 1: {not 1}')
print(f'not False: {not False}')
print(f'not True: {not True}')



