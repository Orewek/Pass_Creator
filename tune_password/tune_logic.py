import datetime


def tune_special_symbols(password: str, chars: str) -> str:
    """
    have a str of chars that we need to remove
    removes that by .replace
    """
    for char in chars:
        password = password.replace(char, '')
    return password


def sanitize_password(password: str, types: str) -> str:
    """
    changes lower => upper; upper => lower; deleting digits from the password
    """
    if 'up' in types:
        password = password.lower()
    if 'low' in types:
        password = password.upper()
    if 'dig' in types:
        password = ''.join([i for i in password if not i.isdigit()])

    return password


def add_comments(password: str, comment: str) -> str:
    """
    adding comment to password
    pass + comment + data info about password
    data - length, creation data, etc
    """
    data = ' // '
    creation_date = datetime.datetime.now()
    if '-time' in comment:
        comment = comment.replace('-time', '')
        data += f'creation date - {creation_date}' + ' // '

    if '-len' in comment:
        comment = comment.replace('-len', '')
        data += f'length - {len(password)}'

    password += ' ' + comment + data

    return password


if __name__ == '__main__':
    print('u cant run this file as main!')
