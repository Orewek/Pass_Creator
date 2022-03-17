import secrets
import os
from tune_password.tune_io import symbols_io, comments_io  # importing our fun's


def main():
    # choosing length for the password
    print("which len do we need")
    length = int(input())

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("write for which acc/game u will use it")
    name_tag = str(input())

    password = name_tag + "_" + secrets.token_urlsafe(10**5)
    password = symbols_io(password)[:length]

    print(f'\npassword was created successfully! the pass is - {password} \n')
    password = comments_io(password)
    print(password)

    # saving this password in our .txt file
    '''
    with open("pass_save.txt", "a+") as f:
        f.write(f"\n{password}")

    print('do we need to add one more password? \n'
          'type smth if yes, or just press enter if no')
    '''
    os.system("pause")


if __name__ == '__main__':
    main()
    # import send_to_ds
