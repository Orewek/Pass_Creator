# -*- coding: utf-8 -*-
"""File contains logic of functions, which saves the password into .txt file."""
def default_save(password: str, default_path: str) -> None:
    """
    Add a new password to the default path file.
    default_path = r'C:[back slash]passwords.txt'

    Args:
    ----
        password: User password
        default_path: path where to save a password from the code
    """
    with open(default_path, "a+", encoding="UTF-8") as f:
        lines = f.readlines()
        if len(lines) == 0:
            f.write(f"{password}\n")
        elif lines[-1].endswith("\n"):
            f.write(f"{password}\n")
        else:
            f.write(f"\n{password}")


def user_path_save(password: str, txt_path: str) -> None:
    """
    Add a new password to a user-path file.
    
    Args:
    ----
        password: User password
        txt_path: User txt path where to save a password
    """
    path = rf'{txt_path}'
    with open(path, "a+", encoding="UTF-8") as f:
        lines = f.readlines()
        if len(lines) == 0:
            f.write(f"{password}\n")

        elif lines[-1].endswith("\n"):
            f.write(f"{password}\n")

        else:
            f.write(f"\n{password}")


if __name__ == '__main__':
    print('u cant run this file as main')
