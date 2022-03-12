def checkslash(password: str) -> str:
    items = ['_', '-']
    possibilities = {'y', 'yes', '1'}

    for i in range(len(items)):
        print(f'do we need to remove {items[i]} in password? write 1, y, yes')
        check_letter = input()

        if(check_letter.lower() in possibilities):
            password = password.replace(f'{items[i]}', '')

    return password


def up_low_dig(password: str) -> str:
    items = ['upper letters', 'lower letters', 'digits']
    possibilities = {'y', 'yes', '1'}

    for i in range(len(items)):
        print(f'do we need to remove {items[i]}? write 1, y, yes')
        check_letter = input()

        if(check_letter.lower() in possibilities):
            password = [
                password.lower(),
                password.upper(),
                ''.join([i for i in password if not i.isdigit()]),
            ][i]
    return password
