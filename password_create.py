import secrets
import tune_password as tp


if __name__ == '__main__':
    print("which len we need")
    length = int(input())

    print("write for which acc/game u will use it")
    name_tag = str(input())

    password = secrets.token_urlsafe(length)
    password = password + "_" + name_tag
    password = tp.up_low_dig(tp.checkslash(password))
    print(password)

'''
with open("pass_save.txt", "a") as f:
    f.write(password)
'''
