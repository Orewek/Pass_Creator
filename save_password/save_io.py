from typing import Union

from save_password.save_logic import default_save, user_path_save


def save_into_txt_io(password: str) -> str:
    """
    as the default password will be saved into C:{back_slash}passwords.txt
    otherwise password will be saved into user path.

    If this file doesnt exist, it will be created
    D:\new_file.txt will be created, but not \new_folder\new_file.txt
    Because folder doesnt exist
    """

    default_path = r'C:\passwords.txt'

    print(f"""
           now you can choose where you want to save your password
           write path to a file, and program will save your password into it
           Press enter and program will create and save a file at {default_path}
           """)

    txt_path: Union[str, None] = input() or None

    if txt_path is None:
        default_save(password, default_path)
        print(f'Your password was succesfully saved into {default_path}')

    else:
        user_path_save(password, txt_path)
        print(f'Your password was succesfully saved into {txt_path}')

    if txt_path is not None:
        return txt_path
    return default_path


if __name__ == '__main__':
    print('u can run this file as main')
