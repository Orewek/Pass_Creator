from save_password.save_logic import default_save, user_path_save


def save_into_txt_io(password: str):
    default_path = r'C:\passwords.txt'

    print('now you can choose where you want to save your password \n'
          'write your path to the txt file, and program will save your password into it! \n'
          f'You can press enter, and program will create a txt file at {default_path} and save into it \n')

    txt_path = input() or None

    if txt_path is None:
        default_save(password, default_path)
        print(f'Your password was succesfully saved into {default_path}')

    else:
        user_path_save(password, txt_path)
        print(f'Your password was succesfully saved into {txt_path}')

    return txt_path


if __name__ == '__main__':
    print('u can run this file as main')
