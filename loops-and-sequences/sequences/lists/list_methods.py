import os

# Lists and their methods

# Basic sintax, just remember
# ['item_1', 'item_2'...'item_n']
# Yeah, ojito on those []

def clear_screen():
    # clears the console screen in a
    # cross-platform manner
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (POSIX systems)
    else:
        _ = os.system('clear')

def print_bar():
    print('---------------\n')


def basic_sintax():
    print_bar()

    cities = ['Los Angeles', 'London', 'Tokyo']
    print('Basic sintax\n')
    # how to use index
    print(f'First item:\ncities[0]: {cities[0]}\n')

    # negative index
    print(f'Negative index:\ncities[-1]: {cities[-1]}\n')
    print(f'List\n{cities}\n')


def another_way():
    print_bar()

    # another way to create a list
    # with list()
    developer_name = 'Jessica'
    print(f'Another way to create lists with list()\n{list(developer_name)}\n')


def total_elements():
    print_bar()

    # to get the total elements in a list
    numbers = [1, 2, 3, 4, 5]
    print(f'Total elements in a list with len()\nList:\n{numbers}\nLength: {len(numbers)}\n')


def update_values():
    print_bar()

    # to update a value
    print('To update values\n')
    programming_languages = ['Python', 'Java', 'C++', 'Rust']
    print(f'List:\n{programming_languages}\n')
    programming_languages[0] = 'JavaScript'
    print(f'Updated:\nprogramming_languages[0]\n{programming_languages}\n')


def beyond_index():
    print_bar()

    # NOTE: If you try to access something beyond the
    # bounds of the list, you'll get an IndexError

    programming_languages = ['Python', 'Java', 'C++', 'Rust']

    print('You can\'t go beyond something in the list\n')
    print('programming_languages[10] = \'JavaScript\'')

    try:
        programming_languages[10] = 'JavaScript'
    except Exception as e:
        print(f'An exception ocurred: {type(e).__name__}')
        print(f'Error message: {e}\n')


def remove_index():
    print_bar()

    # to remove an index, use del keyword
    print('Remove an index with del keyword\n')
    print('developer:')
    developer = ['Jane Doe', 23, 'Python Developer']
    print(developer)
    del developer[1]
    print(f'Deleted: developer[1]\n{developer}\n')


def inside_list():
    print_bar()

    # use of the 'in' keyword
    print('in keyword\n')
    programming_languages = ['Python', 'Java', 'C++', 'Rust']
    print(f'List:\n{programming_languages}')
    print('Rust in list\n', 'Rust' in programming_languages) # True
    print('JavaScript in list\n', 'JavaScript' in programming_languages, '\n') # False


def nested_lists():
    print_bar()

    # nested lists
    print('Nested lists\n')
    developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
    print(f'List:\n{developer}')
    print('developer[2]:', developer[2]) # ['Python', 'Rust', 'C++']
    print('developer[2][1]:', developer[2][1]) # Rust
    # See this? Kinda like an (x, y),
    # (i, j), type of stuff.

    print()


def unpack_list():
    print_bar()

    # unpacking means assigning a value
    # from a list to new variables
    print('Unpacking\n')
    developer = ['Alice', 34, 'Rust Developer']
    print(f'List:\n{developer}\nEach one goes to a new variable\n')
    name, age, job = developer

    print(f'name: {name}') # 'Alice'
    print(f'age: {age}') # 34
    print(f'job: {job}\n') # 'Rust Developer'


def rest_of():
    print_bar()

    # lets you collect the remaining from a list
    # with the * operator
    print('Rest of\n')
    developer = ['Alice', 34, 'Rust Developer']
    print(f'List:\n{developer}\nEach one goes to a new variable\n')
    name, *rest = developer

    print(f'name: {name}') # 'Alice'
    print(f'*rest:\n{rest}\n') # [34, 'Rust Developer']


def when_no_match():
    print_bar()

    # when the values on the left do not
    # match the total numbers of items
    # in the list
    print('When values don\'t match\n')

    try:
        developer = ['Alice', 34, 'Rust Developer']
        name, age, job, city = developer
    except Exception as e:
        print(f'An exception ocurred: {type(e).__name__}')
        print(f'Error message: {e}\n')


def slice_operator():
    print_bar()

    # similar to strings, we can use this :
    # Seems quite the same. Uses a range
    # [start:end]
    # remember that end does not include
    # the number of index that you write
    print('Slice Operator\n')

    desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
    print(f'List:\n{desserts}\n')
    print(f'desserts[1:4]:\n{desserts[1:4]}\n') # ['Cookies', 'Ice Cream', 'Pie']

    # you can also do interval stuff
    # and determine how many steps to make
    # in a list
    print('Prepare for intervals with [1::2]')
    numbers = [1, 2, 3, 4, 5, 6]

    print(f'List:\n{numbers}\n')
    print(f'numbers[1::2]:\n{numbers[1::2]}\n')


def append_list():
    print_bar()

    # append() adds an item to the
    # end of the list
    print('append() method\n')
    numbers = [1, 2, 3, 4, 5]
    print(f'List:\n{numbers}\nAppend: 6\n')
    numbers.append(6)
    print(f'L:\n{numbers}\n')

    # also you can do this
    numbers_nest = [1, 2, 3, 4, 5]
    even_numbers= [6, 8, 10]
    print(f'List 1:\n{numbers_nest}\nList 2:\n{even_numbers}\n')

    numbers_nest.append(even_numbers)
    print('Notice this will nest the appended list\nnumbers.append(even_numbers)')
    print(f'Appends:\n{numbers_nest}\n')


def extend_list():
    print_bar()

    # extend() adds multiple
    # elements as single ones
    numbers = [1, 2, 3, 4, 5]
    even_numbers = [6, 8, 10]
    print('extend() method\n')
    print(f'List 1:\n{numbers}\nList 2:\n{even_numbers}\n')

    numbers.extend(even_numbers)
    print(f'\nExtended list:\nnumbers.extend(even_numbers)\n{numbers}\n')  


def insert_list():
    print_bar()

    # insert() as its name says
    # adds an element in the index that we
    # select as first parameter
    numbers = [1, 2, 3, 4, 5]
    print('insert() method')
    print(f'List:\n{numbers}')

    print('Insert:\nnumbers.insert(2, 2.5)')
    numbers.insert(2, 2.5)
    print(f'List:\n{numbers}\n')


def remove_item():
    print_bar()

    # remove() takes a values as an argument
    # and it only removes its first ocurrence
    print('remove() method\n')

    numbers = [10, 20, 30, 40, 50, 50]
    print(f'List:\n{numbers}\n')

    numbers.remove(50)
    print('Remove:\nnumbers.remove(50)')
    print(f'List:\n{numbers}\n')
    print('It only removes the first ocurrence\n')    
 
    
def pop_item():
    print_bar()

    # pop() returns an element in
    # a specific index
    print('pop() method\n')

    numbers = [1, 2, 3, 4, 5]
    print(f'List:\n{numbers}\n')

    numbers.pop(1)
    print('Pop:\nnumbers.pop(1)')
    print(f'List:\n{numbers}\n')  
    
    # if nothing is passed then it pops
    # the last element in the list
    numbers.pop()
    print('Pop:\nnumbers.pop()')
    print(f'List:\n{numbers}\n')


def clear_list():
    print_bar()

    # clear() cleans the complete list
    print('clear() method\n')

    numbers = [1, 2, 3, 4, 5]
    print(f'List:\n{numbers}\n')

    numbers.clear()
    print('Clear:\nnumbers.clear()')
    print(f'List:\n{numbers}\n')  


def sort_list():
    print_bar()

    # sort() as its name says, sorts
    # all list elements 
    print('sort() method\n')

    numbers = [19, 2, 35, 1, 67, 41]
    print(f'List:\n{numbers}\n')

    numbers.sort()
    print('Sort:\nnumbers.sort()')
    print(f'List:\n{numbers}\n')  

    # also there is sorted()
    # which creates a new list and does the same
    print('sorted()\nReturns a new list')
    numbers_2 = [19, 2, 35, 1, 67, 41]

    print(f'List:\n{numbers_2}')
    sorted_numbers = sorted(numbers_2)
    print(f'New list:\n{sorted_numbers}\n')


def reverse_list():
    print_bar()

    # reverse() inverts the whole list
    print('reverse() method\n')

    numbers = [6, 5, 4, 3, 2, 1]
    print(f'List:\n{numbers}\n')

    numbers.reverse()
    print('Reverse:\nnumbers.reverse()')
    print(f'List:\n{numbers}\n')  


def index_list():
    print_bar()

    # index() is used to find the index
    # where an element exists
    print('index() method\n')

    programming_languages = ['Rust', 'Java', 'Python', 'C++']
    print(f'List:\n{programming_languages}\n')

    index = programming_languages.index('Java')
    print('Index:\nprogramming_languages.index(\'Java\')')
    print(f'Index:\n{index}\n')  

    try:
        print('Index error:\n')
        error_index = programming_languages.index('JavaScript')
        print(error_index)
    except Exception as e:
        print(f'An exception ocurred: {type(e).__name__}')    
        print(f'Error message: {e}\n')
        


#if __name__ == '__main__':
#    print('\n--- Lists and methods ---\n')
#    basic_sintax()
#    another_way()
#    total_elements()
#    update_values()
#    beyond_index()
#    remove_index()
#    inside_list()
#    nested_lists()
#    unpack_list()
#    rest_of()
#    when_no_match()
#    slice_operator()
#    append_list()
#    extend_list()
#    insert_list()
#    remove_item()
#    pop_item()
#    clear_list()
#    sort_list()
#    reverse_list()
#    index_list()
