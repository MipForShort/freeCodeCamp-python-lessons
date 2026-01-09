import os

# =====================================
# Tuples in Python
# =====================================

def print_bar():
    print("------------\n")

def clear_screen():
    # clears the console screen in a
    # cross-platform manner
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (POSIX systems)
    else:
        _ = os.system('clear')

# =====================================
# Tuple syntax
# =====================================

def basic_syntax():
    print_bar()

    print("Basic Syntax")
    print("Tuples are similar to lists, but they use parentheses () instead of brackets [].\n")

    developer = ("Alice", 34, "Rust Developer")

    print(f"Tuple:\n{developer}\n")
    print("Tuples are immutable, meaning their values cannot be changed.\n")


def access_tuple():
    print_bar()

    print("Accessing Tuple Elements")
    print("You can access elements using indexes, just like lists.\n")

    developer = ("Alice", 34, "Rust Developer")

    print(f"Tuple:\n{developer}\n")
    print(f"developer[1]:\n{developer[1]}\n")

    print("Negative indexes also work:")
    print(f"developer[-1]:\n{developer[-1]}\n")

    print("Trying to access an index out of range raises an IndexError.\n")


def make_tuple():
    print_bar()

    print("Creating Tuples")
    print("You can create a tuple using the tuple() constructor.\n")

    developer = "Jessica"

    print(f"Original string:\n{developer}\n")
    print("tuple(developer):")
    print(tuple(developer))
    print()


def in_tuple():
    print_bar()

    print("Using the 'in' Keyword")
    print("Use 'in' to check if a value exists inside a tuple.\n")

    programming_languages = ("Python", "Java", "C++", "Rust")

    print(f"Tuple:\n{programming_languages}\n")

    print("'Rust' in programming_languages:")
    print("Rust" in programming_languages)

    print("\n'JavaScript' in programming_languages:")
    print("JavaScript" in programming_languages)
    print()


def unpack_tuple():
    print_bar()

    print("Tuple Unpacking")
    print("You can unpack tuple values into multiple variables.\n")

    developer = ("Alice", 34, "Rust Developer")
    name, age, job = developer

    print(f"Tuple:\n{developer}\n")
    print("Unpacked values:")
    print("name:", name)
    print("age:", age)
    print("job:", job)
    print()


def rest_tuple():
    print_bar()

    print("Using *rest in Tuple Unpacking")
    print("*rest stores remaining values in a list.\n")

    developer = ("Alice", 34, "Rust Developer")
    name, *rest = developer

    print(f"Tuple:\n{developer}\n")
    print("name:", name)
    print("rest:", rest)
    print()


def slice_tuple():
    print_bar()

    print("Slicing Tuples")
    print("Slicing works the same way as lists: tuple[start:end:step]\n")

    desserts = ("cake", "pie", "cookies", "ice cream")

    print(f"Tuple:\n{desserts}\n")
    print("desserts[1:3]:")
    print(desserts[1:3])
    print()


# =====================================
# Tuple methods
# =====================================

def count_tuple():
    print_bar()

    print("count() Method")
    print("Use tuple.count(value) to count occurrences.\n")

    programming_languages = ("Rust", "Java", "Python", "C++", "Rust")

    print(f"Tuple:\n{programming_languages}\n")
    print("Count of 'Rust':")
    print(programming_languages.count("Rust"))

    print("\nCount of 'JavaScript':")
    print(programming_languages.count("JavaScript"))

    print("\nIf the value is not found, count() returns 0.")
    print("Calling count() without arguments raises a TypeError.\n")


def index_tuple():
    print_bar()

    print("index() Method")
    print("Use tuple.index(value, start, end) to find the position of a value.\n")

    programming_languages = ("Rust", "Java", "Python", "C++", "Rust")

    print(f"Tuple:\n{programming_languages}\n")

    print("First occurrence of 'Rust':")
    print(programming_languages.index("Rust"))

    print("\nSearching for 'Rust' starting from index 1:")
    print(programming_languages.index("Rust", 1))

    print("\nSearching for 'Python' between indexes 1 and 4:")
    print(programming_languages.index("Python", 1, 4))

    print("\nIf the value is not found, index() raises a ValueError.\n")


# =====================================
# sorted() with tuples
# =====================================

def sorted_tuple():
    print_bar()

    print("sorted() Function")
    print("sorted() is NOT a tuple method.")
    print("It returns a new LIST.\n")

    numbers = (5, 2, 9, 1, 7)

    print(f"Original tuple:\n{numbers}\n")

    print("Sorted ascending:")
    print(sorted(numbers))

    print("\nSorted descending:")
    print(sorted(numbers, reverse=True))

    words = ("banana", "apple", "kiwi", "strawberry")

    print(f"\nWords tuple:\n{words}\n")

    print("Sorted by length (key=len):")
    print(sorted(words, key=len))

    print("\nSorted by length, descending:")
    print(sorted(words, key=len, reverse=True))

    print("\nRemember: tuples are immutable, so sorting creates a new list.\n")


# =====================================
# Main execution
# =====================================

'''
if __name__ == "__main__":

    print("\n--- Tuples in Python ---\n")

    basic_syntax()
    access_tuple()
    make_tuple()
    in_tuple()
    unpack_tuple()
    rest_tuple()
    slice_tuple()
    count_tuple()
    index_tuple()
    sorted_tuple()
'''
