# Welcome to some notes for some common
# string methods that FCC provides

print('\n--- String Methods ---\n')

# upper()
# Returns a new string with all characters to uppercase
my_str = 'hello world' 
#print('upper()')
#print(my_str.upper(), '\n')

# Bruh, checkout these next new lines
print(f'upper()\n{my_str.upper()}\n')

# lower()
# Returns a new string with all charactes to lowercase
my_str = 'Hello World'
#print('lower()')
#print(my_str.lower(), '\n')

print(f'lower()\n{my_str.lower()}\n')

# strip()
# Returns a new string trailing characters to remove
# If no arguments passed, it checks for whitespace
my_str = '  hello world  '
#print('strip()')
#print(my_str.strip(), '\n')

print(f'strip()\n{my_str.strip()}\n')

# replace(old, new)
# Replaces all old material some for new stuff
my_str = 'hello world'
#print('replace(old, new)')#
#print(my_str.replace('hello', 'hi'), '\n')#

print(f'replace(old, new)\n{my_str.replace('hello', 'hi')}\n')

# split(separator)
# Splits a string on a specified separator
# into a list of strings. If no separator
# specified, it splits on whitespace
my_str = 'hello world'
#print('split(separator)')
#print(my_str.split(), '\n')

print(f'split(separator)\n{my_str.split()}\n')

# join(iterable)
# Joins an element of an iterable 
# into a string with a separator
my_list = ['hello', 'world']
#print('join(iterable)')
#print(' '.join(my_list), '\n')

print(f'join(iterable)\n{' '.join(my_list)}\n')

# startswith(prefix) 
# Returns a boolean indicating if a
# string starts with the specified
# prefix
my_str = 'hello world'
#print('startswith(prefix)')#
#print(my_str.startswith('hello'), '\n')#

print(f'startswith(prefix)\n{my_str.startswith('hello')}\n')

# endswith(suffix)
# Returns a boolean indicating if a
# string ends with the specified
# suffix
my_str = 'hello world'
#print('endswith(suffix)')
#print(my_str.endswith('world'), '\n')

print(f'endswith(suffix)\n{my_str.endswith('world')}\n')

# find(substring)
# Returns the number of times a substring
# appears in a string
my_str = 'hello world'
#print('find(substring)')
#print(my_str.find('world'), '\n')

print(f'find(substring)\n{my_str.find('world')}\n')

# count(substring)
# Returns the number of times
# a substring appears in
# a string
my_str = 'hello world'
#print('count(substring)')
#print(my_str.count('o'), '\n')

print(f'count(substring)\n{my_str.count('o')}\n')

# capitalize()
# Returns a new string with the first
# character capitalized and the
# other characters lowercased
my_str = 'hello world'
#print('capitalize()')
#print(my_str.capitalize(), '\n')

print(f'capitalize()\n{my_str.capitalize()}\n')

# isupper()
# Returns True if all letters in the
# string are uppercase and False
# if not
my_str = 'hello world'
#print('isupper()')
#print(my_str.isupper(), '\n')

print(f'isupper()\n{my_str.isupper()}\n')

# islower()
# Return True if all letters in the
# string are lowercase and False
# if not
my_str = 'hello world'
#print('islower()')
#print(my_str.islower(), '\n')

print(f'islower()\n{my_str.islower()}\n')

# title()
# Returns a new string with the
# first letter of each word
# capitalized
my_str = 'hello world'
#print('title()')
#print(my_str.title(), '\n')

print(f'title()\n{my_str.title()}\n')