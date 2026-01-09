import list_methods as lm

print('\n--- Welcome to the list and methods file ---\n')

MAIN_MENU = '''
--- Select what to see ---
1. List syntax
2. List methods
0. Exit
Option: '''

SYNTAX_MENU = '''
--- List Syntax ---
1. Basic syntax
2. Another way
3. Total elements
4. Update values
0. Back
Option: '''

SYNTAX_ACTIONS = {
    1: lm.basic_syntax,
    2: lm.another_way,
    3: lm.total_elements,
    4: lm.update_values
}

METHODS_MENU = '''
--- List Methods ---
1. Append
2. Extend
3. Insert
4. Remove
5. Pop
6. Clear
7. Sort
8. Reverse
9. Index
0. Back
Option: '''

METHODS_ACTIONS = {
    1: lm.append_list,
    2: lm.extend_list,
    3: lm.insert_list,
    4: lm.remove_item,
    5: lm.pop_item,
    6: lm.clear_list,
    7: lm.sort_list,
    8: lm.reverse_list,
    9: lm.index_list
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
        lm.clear_screen()
        option = get_option(menu_text, actions.keys() | {0})

        if option == 0:
            break

        action = actions.get(option)
        if action:
            lm.clear_screen()
            action()
            input("\nPress Enter to continue...")


def main():
    while True:
        lm.clear_screen()
        option = get_option(MAIN_MENU, {0, 1, 2})

        if option == 0:
            break
        elif option == 1:
            submenu(SYNTAX_MENU, SYNTAX_ACTIONS)
        elif option == 2:
            submenu(METHODS_MENU, METHODS_ACTIONS)

if __name__ == '__main__':
    main()


