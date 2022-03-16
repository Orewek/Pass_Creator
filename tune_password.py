def tune_io(password: str) -> str:
    items = ['_', '-']

    print(f'choose and write symbobls from {items} '
          f'without spaces and commas that we need to delete \n'
          f'if u dont need to press enter')

    symbols = input()
    if symbols is not None:
        password = tune_symbols(password, symbols)

    items = ['up', 'low', 'dig']
    print(f'choose and write words from {items} '
          f'without spaces and commas that we need to delete \n'
          f'if u dont need to press enter \n'
          f'for example: low deleting whole lower letters from the pass')

    symbols = input()
    if symbols is not None:
        password = up_low_dig(password, symbols)

    return password


def tune_symbols(password: str, chars: str) -> str:
    for char in chars:
        password = password.replace(char, '')
    return password


def up_low_dig(password: str, types: str) -> str:
    # removes leters/digits from the pass if we need to
    if 'up' in types:
        password = password.lower()
    if 'low' in types:
        password = password.upper()
    if 'dig' in types:
        password = ''.join([i for i in password if not i.isdigit()])

    return password


if __name__ == '__main__':
    print('u cant run this file as main!')
