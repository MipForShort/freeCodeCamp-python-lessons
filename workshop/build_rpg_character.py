
full_dot = '●'
empty_dot = '○'

def validate_name(name):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'

def validate_stats(STR, INT, CHA):
    for stat in (STR, INT, CHA):
        if not isinstance(stat, int):
            return 'All stats should be integers'
        elif stat < 1:
            return 'All stats should be no less than 1'
        elif stat > 4:
            return 'All stats should be no more than 4'
    if (STR + INT + CHA) != 7:
        return 'The character should start with 7 points'

def dots(stat):
    return (stat * full_dot) + ((10 - stat) * empty_dot) 

def create_character(name, STR, INT, CHA):
    name_err = validate_name(name)
    stat_err = validate_stats(STR, INT, CHA)
    if name_err:
        return name_err
    elif stat_err:
        return stat_err
    else:
        return (
            f'{name}\n'
            f'STR {dots(STR)}\n'
            f'INT {dots(INT)}\n'
            f'CHA {dots(CHA)}'
        )


print(create_character('ren', 4, 2, 1))
