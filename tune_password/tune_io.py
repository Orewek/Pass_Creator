from tune_password.tune_logic import tune_symbols, up_low_dig, add_comments


def symbols_io(password: str) -> str:
    items = ['_', '-']

    print(f'choose and write symbobls from {items} '
          f'without spaces and commas that we need to delete \n'
          f'if u dont need to press enter')

    symbols = input()
    if symbols is not None:
        password = tune_symbols(password, symbols)

    items = ['up', 'low', 'dig']
    print(f'choose and write words from {items} that we need to delete \n'
          f'if u dont need to press enter \n'
          f'for example: low deleting whole lower letters from the password')

    symbols = input()
    if symbols is not None:
        password = up_low_dig(password, symbols.lower())

    return password


def comments_io(password: str) -> str:
    print('U can add some comments to password, it can help u if: \n'
          'U have a few accs in 1 app (steam for example). '
          'U wanna see the creation data, length etc. \n'
          'firsly write u commentary, after that (-time: creation data), (-len: length)'
          'press enter u dont want to have it')

    comment = str(input())
    if comment is not None:
        password = add_comments(password, comment)

    return password


if __name__ == '__main__':
    print('u cant run this file as main!')
