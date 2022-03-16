import secrets
import tune_password as tp  # importing our fun's


if __name__ == '__main__':
    # choosing length for the password
    print("which len do we need")
    length = int(input())

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("write for which acc/game u will use it")
    name_tag = str(input())

    password = secrets.token_urlsafe(10**5)
    password = name_tag + "_" + password
    password = tp.tune_io(password)

    print(password[:length])


'''
# saving this password in our .txt file
with open("pass_save.txt", "a") as f:
    f.write(password)
'''
