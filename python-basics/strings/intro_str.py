print('\n--- String types ---\n')

# String types
str_1 = 'Hello'
str_2 = "World"

str_3 = """Multiline
string
"""
str_4 = '''Another
multiline
string
'''

print(f'Simple strings:\n{str_1}\n{str_2}\n\nMultiline strings:\n{str_3}\n{str_4}')

# Opposite quotation
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(f'Opposite quotation:\n{msg}\n{quote}\n')

# Escape
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(f'Escape:\n{msg}\n{quote}\n')

my_str = 'Hello world'

# in operator
print('In operator')
print('Hello' in my_str)
print('hey' in my_str)
print('hi' in my_str)
print('e' in my_str)
print('f' in my_str)
print('\n' in my_str, '\n')

# Length
print(f'Length:\n{len(my_str)}\n')

# Index
print('Index')
print(my_str[0])
print(my_str[6], '\n')

# Negative index does reverse
print('Reverse index')
print(my_str[-1])
print(my_str[-2], '\n')

# Immutable strings
greeting = 'hi'
greeting = 'hello'
print(greeting)

# Cannot change index on string
greeting = 'hi'
# greeting[0] = 'H'

