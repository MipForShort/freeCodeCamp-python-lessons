print('\n---Data Types---\n')

# Integer
int_var = 10
print('Integer:', int_var)
print(type(int_var), '\n')

# Float
float_var = 4.50
print('Float:', float_var)
print(type(float_var), '\n')

# String
str_var = 'hello'
print('String:', str_var)
print(type(str_var), '\n')

# Boolean
bool_var_t = True
bool_var_f = False
print(f'Boolean: {bool_var_t}\nBoolean: {bool_var_f}')
print(type(bool_var_t), type(bool_var_f), '\n')

# Set
set_var = {7, 5, 8}
print('Set:', set_var)
print(type(set_var), '\n')

# Dictionary
dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', dictionary_var)
print(type(dictionary_var), '\n')

# Tuple
tuple_var = (7, 5, 8)
print('Tuple:', tuple_var)
print(type(tuple_var), '\n')

# Range
range_var = range(5)
print('Range:', range_var)
print(type(range_var), '\n')

# List
my_list = [22, 'Hello world', 3.14, True]
print(my_list)
print(type(my_list), '\n')

# None (Special value)
none_var = None
print('None:', none_var)
print(type(none_var), '\n')

# Instance examples
print(isinstance('Hello world', str)) # True
print(isinstance(True, bool)) # True
print(isinstance(42, int)) # True
print(isinstance('John Doe', int)) # False