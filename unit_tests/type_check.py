# -*- coding: utf-8 -*-
"""Int and action check for variables."""


def action_check(actions: str) -> bool:
    """Maybe user wrote wrong digit or even a letter.
    
    Args:
    ----
        actions: user input to choose smth from the table

    Return:
    ------
        True: all ok
        False: User wrote smth except [1-6]
    """
    for i in range(1, 6 + 1):
        actions = actions.replace(f'{i}', '')

    if actions == '':
        return True

    return False


def check_int(variable: int | str, text_error: str) -> int:
    """Check is the variable type int, otherwise reinput till int.
    
    Args:
    ----
        variable: Some variable that we check to be int
        text_error: raise textError if not, reinput till int
    
    Return: return variable with int type
    ------
    """
    while variable.isdigit() is False:
        variable = input(text_error)

    return int(variable)


if __name__ == '__main__':
    print('You cant run this file as main')
