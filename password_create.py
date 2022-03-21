import secrets
import os
from tune_password.tune_io import remove_excess_password_io, comments_to_password_io
from save_password.save_io import save_into_txt_io
from what_send_ds.what_send_io import what_send_ds_io
from send_to_ds import bot


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
    txt_path = save_into_txt_io(password)

    # choosing which path should bot send to ds
    res_path = what_send_ds_io(txt_path)

    '''
    # imma do this later
    print('do we need to add one more password? \n'
          'type smth if yes, or just press enter if no')
    '''

    os.system("pause")
    # starting bot
    bot(res_path)


if __name__ == '__main__':
    main()
