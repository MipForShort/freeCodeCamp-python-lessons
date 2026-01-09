import tuple_methods as tm

print("\n--- Welcome to the Tuples and Methods file ---\n")

MAIN_MENU = """
--- Select what to see ---
1. Tuple syntax
2. Tuple methods
0. Exit
Option: """
    

SYNTAX_MENU = """
--- Tuple Syntax ---
1. Basic syntax
2. Access elements
3. Create tuples
4. Membership (in)
5. Unpacking
6. *rest unpacking
7. Slicing
0. Back
Option: """


SYNTAX_ACTIONS = {
    1: tm.basic_syntax,
    2: tm.access_tuple,
    3: tm.make_tuple,
    4: tm.in_tuple,
    5: tm.unpack_tuple,
    6: tm.rest_tuple,
    7: tm.slice_tuple,
}


METHODS_MENU = """
--- Tuple Methods ---
1. Count
2. Index
3. Sorted
0. Back
Option: """


METHODS_ACTIONS = {
    1: tm.count_tuple,
    2: tm.index_tuple,
    3: tm.sorted_tuple,
}


def get_option(prompt, valid_options):
    try:
        option = int(input(prompt))
        if option in valid_options:
            return option
    except ValueError:
        pass
    return None


def submenu(menu_text, actions):
    while True:
        tm.clear_screen()
        option = get_option(menu_text, actions.keys() | {0})

        if option == 0:
            break

        action = actions.get(option)
        if action:
            tm.clear_screen()
            action()
            input("\nPress Enter to continue...")


def main():
    while True:
        tm.clear_screen()
        option = get_option(MAIN_MENU, {0, 1, 2})

        if option == 0:
            break
        elif option == 1:
            submenu(SYNTAX_MENU, SYNTAX_ACTIONS)
        elif option == 2:
            submenu(METHODS_MENU, METHODS_ACTIONS)


if __name__ == "__main__":
    main()
