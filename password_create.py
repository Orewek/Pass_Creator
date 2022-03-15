import secrets
import unittest
import tune_password as tp  # importing our fun's
from test_password import TestPassword

if __name__ == '__main__':
    # choosing length for the password

    TestPassword(unittest.TestCase)
    print("which len do we need")
    length = int(input())

    # writing the game/for which for we will use this pass
    # we make it for ctrl + f in file

    print("write for which acc/game u will use it")
    name_tag = str(input())

    password = secrets.token_urlsafe(length)
    password = password + "_" + name_tag
    password = tp.up_low_dig(tp.checkslash(password, 1), 1)

    print(password)


'''
# saving this password in our .txt file
with open("pass_save.txt", "a") as f:
    f.write(password)
'''
