from learn_password.learn_logic import letter_to_word


def learn_io(password: str):
    """
    every letter, number etc. turns into word, which begins by this letter
    for example: a - apple, U - USA
    """

    remember_password = letter_to_word(password)
    print(f'Remember your password:\n{remember_password}\n'
          f'Copy or write that on the paper, program will NOT save this words! \n')


if __name__ == '__main__':
    print('u can run this file as main')
