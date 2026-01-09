import os

# =====================================
# Utility functions
# =====================================

def clear_screen():
    """
    Clears the console screen in a cross-platform way.
    """
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")


def print_bar():
    print("---------------\n")


# =====================================
# List syntax
# =====================================

def basic_syntax():
    print_bar()

    print("Basic Syntax\n")
    cities = ["Los Angeles", "London", "Tokyo"]

    print("First element:")
    print(f"cities[0]: {cities[0]}\n")

    print("Negative index:")
    print(f"cities[-1]: {cities[-1]}\n")

    print("Full list:")
    print(cities)
    print()


def another_way():
    print_bar()

    print("Creating Lists with list()\n")
    developer_name = "Jessica"
    print(list(developer_name))
    print()


def total_elements():
    print_bar()

    print("Total Elements with len()\n")
    numbers = [1, 2, 3, 4, 5]

    print(f"List:\n{numbers}")
    print(f"Length: {len(numbers)}\n")


def update_values():
    print_bar()

    print("Updating List Values\n")
    programming_languages = ["Python", "Java", "C++", "Rust"]

    print(f"Original list:\n{programming_languages}\n")

    programming_languages[0] = "JavaScript"
    print("Updated list:")
    print(programming_languages)
    print()


def beyond_index():
    print_bar()

    print("Accessing Out-of-Range Indexes\n")
    programming_languages = ["Python", "Java", "C++", "Rust"]

    print("Trying to assign a value beyond list bounds:")
    print("programming_languages[10] = 'JavaScript'\n")

    try:
        programming_languages[10] = "JavaScript"
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Error message: {e}\n")


def remove_index():
    print_bar()

    print("Removing an Element by Index (del)\n")
    developer = ["Jane Doe", 23, "Python Developer"]

    print("Original list:")
    print(developer)

    del developer[1]
    print("\nAfter deleting index 1:")
    print(developer)
    print()


def inside_list():
    print_bar()

    print("Membership Test with 'in'\n")
    programming_languages = ["Python", "Java", "C++", "Rust"]

    print(f"List:\n{programming_languages}\n")
    print("'Rust' in list:", "Rust" in programming_languages)
    print("'JavaScript' in list:", "JavaScript" in programming_languages)
    print()


def nested_lists():
    print_bar()

    print("Nested Lists\n")
    developer = ["Alice", 25, ["Python", "Rust", "C++"]]

    print(f"List:\n{developer}")
    print("developer[2]:", developer[2])
    print("developer[2][1]:", developer[2][1])
    print()


def unpack_list():
    print_bar()

    print("List Unpacking\n")
    developer = ["Alice", 34, "Rust Developer"]

    print(f"List:\n{developer}\n")

    name, age, job = developer
    print("Unpacked values:")
    print("name:", name)
    print("age:", age)
    print("job:", job)
    print()


def rest_of():
    print_bar()

    print("Using *rest in Unpacking\n")
    developer = ["Alice", 34, "Rust Developer"]

    name, *rest = developer
    print("name:", name)
    print("rest:", rest)
    print()


def when_no_match():
    print_bar()

    print("Unpacking Mismatch\n")

    try:
        developer = ["Alice", 34, "Rust Developer"]
        name, age, job, city = developer
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Error message: {e}\n")


def slice_operator():
    print_bar()

    print("Slice Operator\n")
    desserts = ["Cake", "Cookies", "Ice Cream", "Pie", "Brownies"]

    print(f"List:\n{desserts}\n")
    print("desserts[1:4]:")
    print(desserts[1:4])
    print()

    print("Using step values [1::2]")
    numbers = [1, 2, 3, 4, 5, 6]

    print(f"List:\n{numbers}")
    print("numbers[1::2]:")
    print(numbers[1::2])
    print()


# =====================================
# List methods
# =====================================

def append_list():
    print_bar()

    print("append() Method\n")
    numbers = [1, 2, 3, 4, 5]

    print(f"Original list:\n{numbers}")
    numbers.append(6)

    print("\nAfter append(6):")
    print(numbers)
    print()

    numbers_nested = [1, 2, 3]
    even_numbers = [4, 6, 8]

    print("Appending a list creates a nested list:")
    numbers_nested.append(even_numbers)
    print(numbers_nested)
    print()


def extend_list():
    print_bar()

    print("extend() Method\n")
    numbers = [1, 2, 3, 4, 5]
    even_numbers = [6, 8, 10]

    print(f"List 1:\n{numbers}")
    print(f"List 2:\n{even_numbers}\n")

    numbers.extend(even_numbers)
    print("After extend():")
    print(numbers)
    print()


def insert_list():
    print_bar()

    print("insert() Method\n")
    numbers = [1, 2, 3, 4, 5]

    print(f"Original list:\n{numbers}")
    numbers.insert(2, 2.5)

    print("\nAfter insert(2, 2.5):")
    print(numbers)
    print()


def remove_item():
    print_bar()

    print("remove() Method\n")
    numbers = [10, 20, 30, 40, 50, 50]

    print(f"Original list:\n{numbers}")
    numbers.remove(50)

    print("\nAfter remove(50):")
    print(numbers)
    print("Only the first occurrence is removed.\n")


def pop_item():
    print_bar()

    print("pop() Method\n")
    numbers = [1, 2, 3, 4, 5]

    print(f"Original list:\n{numbers}")

    numbers.pop(1)
    print("\nAfter pop(1):")
    print(numbers)

    numbers.pop()
    print("\nAfter pop():")
    print(numbers)
    print()


def clear_list():
    print_bar()

    print("clear() Method\n")
    numbers = [1, 2, 3, 4, 5]

    print(f"Original list:\n{numbers}")
    numbers.clear()

    print("\nAfter clear():")
    print(numbers)
    print()


def sort_list():
    print_bar()

    print("sort() Method\n")
    numbers = [19, 2, 35, 1, 67, 41]

    print(f"Original list:\n{numbers}")
    numbers.sort()

    print("\nAfter sort():")
    print(numbers)
    print()

    print("sorted() Function (creates a new list)")
    numbers_2 = [19, 2, 35, 1, 67, 41]

    sorted_numbers = sorted(numbers_2)
    print("Original:", numbers_2)
    print("Sorted:", sorted_numbers)
    print()


def reverse_list():
    print_bar()

    print("reverse() Method\n")
    numbers = [6, 5, 4, 3, 2, 1]

    print(f"Original list:\n{numbers}")
    numbers.reverse()

    print("\nAfter reverse():")
    print(numbers)
    print()


def index_list():
    print_bar()

    print("index() Method\n")
    programming_languages = ["Rust", "Java", "Python", "C++"]

    print(f"List:\n{programming_languages}\n")

    index = programming_languages.index("Java")
    print("Index of 'Java':")
    print(index)
    print()

    try:
        programming_languages.index("JavaScript")
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Error message: {e}\n")
