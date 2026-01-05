# Functions
print('\n--- Functions ---\n')

# These are reusable pieces of code that
# run when you call them
print('Reusable pieces of code')

# Examples are print(), input(), int(), etc
print('At this point you have seen many examples')
print('input() is a new function for you\nthat allows user input')
print('\nFor better experience on this lesson\nYou need to look at the code\n')

# To define a custom function, just use
# the following structure and their sintax
def hello():
    print('Hello World\n')

# And just call it like this
hello()

# For better use, functions always return something.
# That is, that every time you use a function you get
# a value that generates when the func finishes.

# This only prints, but the return value by default is None 
def calculate_sum(a, b):
    print(a + b)

sum = calculate_sum(3, 1)
print('Sum:', sum, f'\n{type(sum)}\n')

# Now look at a better version
def better_calculate_sum(a, b):
    return a + b

sum = better_calculate_sum(3, 1)

print(f'Sum: {sum}\n{type(sum)}')