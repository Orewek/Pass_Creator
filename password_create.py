import secrets
import os
from tune_password.tune_io import remove_excess_password_io, comments_to_password_io
from save_password.save_io import save_into_txt_io
from learn_password.learn_io import learn_io
from what_send_ds.what_send_io import what_send_ds_io
from ds_bot.send_to_ds import bot

from unit_tests.type_check import action_check


def main():
    """
    Heres user choose what he wanna do
    1. creating a new password, look at create_password()
    2. Removing _ and - from the password -> dota_123hn-asdf-2 / dota123hnasdf2
    3. "special code" for password (to learn it) -> l2U / loop 2 USA
    4. Adding some comments to password -> "password" // length - 30 (-len)
    5. Saving password to .txt file
    6. Turning on the discord bot which can send this .txt to the chat
    """
    switcher = {
        '1': create_password,
        '2': remove_excess_password_io,
        '3': learn_io,
        '4': comments_to_password_io,
        '5': save_into_txt_io,
        '6': bot
    }

    print('\nWtire digits (together) in ascending order:\n'
          'Rememember, You cant make 1 + smth else'
          'u choose  ONLY 1st or 2-6 funs\n'
          '1: create_password\n'
          '2: remove_excess\n'
          '3: learn\n'
          '4: add_comments\n'
          '5: save_into_txt')

    # step which program should do
    actions = str(input())

    # we need to input our password and make smth with that
    while action_check(actions) is False:
        print('This command doesnt exist, try again or close the program')
        actions = str(input())

    if actions != '1':
        print('\nwrite your password\n')
        global password
        password = str(input())

        for i in range(len(actions)):
            # exception cuz:
            # 1. in learn method we dont save anything
            # 2. we dont need this "special code"
            if actions[i] != '3':
                password = switcher[actions[i]](password)
            else:
                switcher[actions[i]](password)

    # we gonna create a new one, so we dont need password = input()
    elif actions == '1':
        for i in range(len(actions)):
            switcher[actions[i]]()


def create_password():
    """
    Create a  new password

    1. choosing length ->  ∈[1; +∞], ∈ ℤ
    2. Writing tag -> tag_password -> dota_SDAjnweg-odsfGB123123
    3. Removing _ and - from the password -> dota_123hn-asdf-2 / dota123hnasdf2
    4. "special code" for password (to learn it) -> l2U / loop 2 USA
    5. Adding some comments to password -> "password" // length - 30 (-len)
    6. Saving password to .txt file
    7. Turning on the discord bot which can send this .txt to the chat
    """
    # choosing length for the password
    print("which len do we need")
    password_length = input()

    while password_length.isdigit() is False:
        print('You cant type a letters in password length, try again')
        password_length = input()
    password_length = int(password_length)


    # change_check(password_length)

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("\nwrite for which acc/game u will use it")
    tag = str(input())

    # adding tag thing. Made that if/else for this "_" thing 
    if tag is not None: tag_password = tag + "_" + secrets.token_urlsafe(3 * password_length)
    else: tag_password = secrets.token_urlsafe(3 * password_length)
    password = remove_excess_password_io(tag_password)[:password_length]

    print(f'\npassword was created successfully! the pass is - {password}')

    # turns letters to words, that helps to remember the password
    if len(password) <= 25:
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
