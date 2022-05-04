import secrets
import os
from tune_password.tune_io import remove_excess_password_io, comments_to_password_io
from save_password.save_io import save_into_txt_io
from learn_password.learn_io import learn_io
from what_send_ds.what_send_io import what_send_ds_io
from send_to_ds import bot


''' user will able to change smth on each stage, coming soon'''
'''
def change_check(user_input: str):
    if user_input == '-change' and in change_str:
        res = change_str.strip().split(' ')
        for count, item in enumerate(res):
            print(count, item)

        change_it()
    if user_input == '-change' and not in change_str:
        print('U cant change rn! complete this input')


def change_it():
    print('fuck yeah!')

change_str = 'password_length tag tag_password password_wo_slash_underscore comment_password txt_path res_path'

def main():
    password_length = input()
    tag = str(input())
    tag_password = tag + "_" + secrets.token_urlsafe(3 * password_length)
    password_wo_slash_underscore = remove_excess_password_io(tag_password)[:password_length]
    comment_password = comments_to_password_io(password_wo_slash_underscore)
    txt_path = save_into_txt_io(comment_password)
    res_path = what_send_ds_io(txt_path)
    bot(res_path)

'''


def main():
    # choosing length for the password
    print("which len do we need")
    password_length = int(input())
    # change_check(password_length)

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("\nwrite for which acc/game u will use it")
    tag = str(input())

    tag_password = tag + "_" + secrets.token_urlsafe(3 * password_length)
    password = remove_excess_password_io(tag_password)[:password_length]

    print(f'\npassword was created successfully! the pass is - {password}')

    # turns letters to words, that helps to remember the password
    learn_io(password)

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
