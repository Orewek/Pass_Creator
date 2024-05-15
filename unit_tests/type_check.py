def action_check(actions: str) -> bool:
    """Maybe user wrote wrong digit or even a letter"""
    for i in range(1, 6 + 1):
        actions = actions.replace(f'{i}', '')
    if actions == '':
        return True
    return False


def check_int(variable: int | str, text_error: str) -> int:
    while variable.isdigit() is False:
        variable = input(text_error)

    return int(variable)


if __name__ == '__main__':
    print('You cant run this file as main')
