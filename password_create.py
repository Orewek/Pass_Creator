import secrets
import tune_password as tp  # importing our fun's


def main():
    # choosing length for the password
    print("which len do we need")
    length = int(input())

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("write for which acc/game u will use it")
    name_tag = str(input())

    password = name_tag + "_" + secrets.token_urlsafe(10**5)
    password = tp.tune_io(password)[:length]

    print(password)

    # saving this password in our .txt file
    with open("pass_save.txt", "a+") as f:
        f.write(f"\n{password}")

    print('do we need to add one more password? \n'
          'type smth if yes, or just press enter if no')


if __name__ == '__main__':
    import send_to_ds
    exec(send_to_ds)
