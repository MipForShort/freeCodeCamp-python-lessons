'''
Docstring for freeCodeCamp.python-basics.functions.scope

Scope for python follows LEGB rule:

    -Local scope (L): Variables defined in functions or classes.
    -Enclosing scope (E): Variables defined in enclosing or nested functions.
    -Global scope (G): Variables defined at the top level of the module or file.
    -Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

Now the examples
'''

# Local

def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

# print(my_var) # NameError: name 'my_var' is not defined

# Enclosing

def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?

# Global

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20

# Built-in
# refers to all of Python's built-in functions,
# modules, and keywords, and are available
# anywhere in your program

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False