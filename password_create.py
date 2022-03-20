import secrets
import os
from tune_password.tune_io import remove_excess_password_io, comments_to_password_io  # importing our fun's
from save_password.save_io import save_into_txt_io


def main():
    # choosing length for the password
    print("which len do we need")
    password_length = int(input())

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("\nwrite for which acc/game u will use it")
    tag = str(input())

    password = tag + "_" + secrets.token_urlsafe(3 * password_length)
    password = remove_excess_password_io(password)[:password_length]

    print(f'\npassword was created successfully! the pass is - {password}')
    password = comments_to_password_io(password)
    print(f'\n{password}\n')

    # saving this password in our .txt file
    save_into_txt_io(password)

    '''
    # imma do this later
    print('do we need to add one more password? \n'
          'type smth if yes, or just press enter if no')
    '''

    os.system("pause")


if __name__ == '__main__':
    main()
    # import send_to_ds
