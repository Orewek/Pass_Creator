from tune_password.tune_logic import tune_special_symbols, sanitize_password, add_comments


def remove_excess_password_io(password: str) -> str:
    """
    firstly removes _ and - for the password
    secondly change lower => upper; upper => lower; removes digits
    """
    items = ['_', '-']

    print(f'\nchoose and write symbobls from {items}'
          f'without spaces and commas that we need to delete \n'
          f'if u dont need to press enter')

    symbols = input()
    if symbols is not None:
        password = tune_special_symbols(password, symbols)

    items = ['up', 'low', 'dig']
    print(f'\nchoose and write words from {items} that we need to delete \n'
          f'if u dont need to press enter \n'
          f'for example: low deleting whole lower letters from the password')

    symbols = input()
    if symbols is not None:
        password = sanitize_password(password, symbols.lower())

    return password


def comments_to_password_io(password: str) -> str:
    """
    adding comment to the password
    it can help you have a few accs in 1 store
    can add some info about password; (-time: creation data), (-len: length)
    """
    print('\nYou can add some comments to password, it can help you if: \n'
          'You have a few accs in 1 app and want to see more information\n'
          'Write your commentary, also you can use this commands:\n'
          '(-time: creation data), (-len: length) \n'
          'press enter if you dont want to have it')

    comment = str(input())
    if comment is not None:
        password = add_comments(password, comment)

    return password


if __name__ == '__main__':
    print('You cant run this file as main!')
