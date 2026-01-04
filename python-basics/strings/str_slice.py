# String slicing 101

print('\n--- String Slice ---\n')

my_str = "Hello world"

print(f'String:\n{my_str}\n')

print("Simple indexes")
print('my_str[i]')
print(my_str[0])
print(my_str[6])
print(my_str[-1], '\n')

# How to slice
# Just do this
# string[start:stop]

print('To slice a string use the next rule\nstring[start:stop]')
print('Example')

print('my_str[1:4]\n', my_str[1:4], '\n')

# You can omit the start or/and stop

print('You can omit the start/stop')
print(f'my_str[:7]\n{my_str[:7]}')
print(f'my_str[8:]\n{my_str[8:]}\n')

# You can omit both

print(f'You can omit both\nmy_str[:]\n{my_str[:]}\n')

# There's a third argument you can pass,
# it is called step, like a for loop

print('You can take steps with a third argument')
print('string[start:stop:step]')
print(f'my_str[0:11:2]\n{my_str[0:11:2]}\n')

# Even backwards with negative numbers

print('Even backwards with negative numbers')
print(f'my_str[::-1]\n{my_str[::-1]}')

