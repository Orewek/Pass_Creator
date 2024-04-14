from learn_password.learn_logic import letter_to_word


def learn_io(password: str) -> None:
    """
    every letter, number etc. turns into  the word, which begins by this letter
    for example: a - apple, U - USA
    """

    remember_password: str = letter_to_word(password)
    print(f"""
           Remember your password:\n{remember_password}
           Copy that, program will NOT save this words!
           """)


if __name__ == '__main__':
    print('You can run this file as main')
