# -*- coding: utf-8 -*-
"""Add comments, remove some chars from the password."""
import datetime as dt


def tune_special_symbols(password: str, chars: str) -> str:
    """
    Have a str of chars that we need to remove.
    removes that by .replace

    Args:
    ----
        password: User password
        chars: chars which we remove from a password
    
    Return:
    ------
        password: User password
    """
    for char in chars:
        password = password.replace(char, '')

    return password


def sanitize_password(password: str, types: str) -> str:
    """
    Change lower => upper; upper => lower; deleting digits from the password.

    Args:
    ----
        password: User password
        types: type of letter that we should remove from a password

    Return:
    ------
        password: User password
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
    Add comment to password.
    pass + comment + data info about password
    data - length, creation data, etc

    Args:
    ----
        password: User password
        comment: User comment that we should add to a password

    Return:
    ------
        password: User password
    """
    data: str = ' // '
    creation_date = datetime.datetime.now(tz=datetime.timezone.utc)
    if '-time' in comment:
        comment = comment.replace('-time', '')
        data += f'creation date - {creation_date}' + ' // '

    if '-len' in comment:
        comment = comment.replace('-len', '')
        data += f'length - {len(password)}'

    if data != ' // ':
        password += ' ' + comment + data
    else:
        password += ' ' + comment

    return password


if __name__ == '__main__':
    print('You cant run this file as main!')
