# Welcome to some notes for some common
# string methods that FCC provides

print('\n--- String Methods ---\n')

# upper()
# Returns a new string with all characters to uppercase
my_str = 'hello world' 
print('upper()')
print(my_str.upper(), '\n')

# lower()
# Returns a new string with all charactes to lowercase
my_str = 'Hello World'
print('lower()')
print(my_str.lower(), '\n')

# strip()
# Returns a new string trailing characters to remove
# If no arguments passed, it checks for whitespace
my_str = '  hello world  '
print('strip()')
print(my_str.strip(), '\n')

# replace(old, new)
# Replaces all old material some for new stuff
my_str = 'hello world'
print('replace(old, new)')
print(my_str.replace('hello', 'hi'), '\n')

# split(separator)
# Splits a string on a specified separator
# into a list of strings. If no separator
# specified, it splits on whitespace
my_str = 'hello world'
print('split(separator)')
print(my_str.split(), '\n')

# join(iterable)
# Joins an element of an iterable 
# into a string with a separator
my_list = ['hello', 'world']
print('join(iterable)')
print(' '.join(my_list), '\n')