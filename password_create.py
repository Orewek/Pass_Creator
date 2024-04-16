import os
import secrets

from ds_bot.send_to_ds import bot

from learn_password.learn_io import learn_io

from save_password.save_io import save_into_txt_io

from tune_password.tune_io import comments_to_password_io, remove_excess_password_io

from unit_tests.type_check import action_check, check_int

from what_send_ds.what_send_io import what_send_ds_io


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
    switcher: dict = {
        '1': create_password,
        '2': remove_excess_password_io,
        '3': learn_io,
        '4': comments_to_password_io,
        '5': save_into_txt_io,
        '6': bot,
    }

    print("""
          Wtire digits (together) in ascending order:
          Rememember, You cant make 1 + smth else
          u choose  ONLY 1st or 2-6 funs
          1: create_password
          2: remove_excess
          3: learn
          4: add_comments
          5: save_into_txt
          """)

    # step which program should do
    actions: str = str(input())

    # we need to input our password and make smth with that
    while action_check(actions) is False:
        actions: str = str(input('This command doesnt exist, try again or close the program'))

    if actions != '1':
        global password
        password: str = str(input('\nwrite your password\n'))

        for i in range(len(actions)):
            # exception cuz:
            # 1. in learn method we dont save anything
            # 2. we dont need this "special code"
            if actions[i] != '3':
                password: str = switcher[actions[i]](password)
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
    password_length: int = check_int(input("which len do we need"),
                                     "You cant type a letters in password length, try again")

    # change_check(password_length)

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    tag: str = str(input("\nwrite for which acc/game u will use it"))

    # adding tag thing. Made that if/else for this "_" thing
    tag_password: str = secrets.token_urlsafe(3 * password_length)
    if tag is not None:
        tag_password: str = tag + "_" + secrets.token_urlsafe(3 * password_length)
    password: str = remove_excess_password_io(tag_password)[:password_length]

    print(f'\npassword was created successfully! the pass is - {password}')

    # turns letters to words, that helps to remember the password
    if len(password) <= 25:
        learn_io(password)

    password: str = comments_to_password_io(password)
    print(f'\n{password}\n')

    # saving this password in our .txt file
    txt_path: str = save_into_txt_io(password)

    # choosing which path should bot send to ds
    res_path: str = what_send_ds_io(txt_path)

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
