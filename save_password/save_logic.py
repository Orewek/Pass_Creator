def default_save(password: str, default_path: str):
    with open(default_path, "a+") as f:
        f.write(f"\n{password}")


def user_path_save(password: str, txt_path: str):
    path = rf'{txt_path}'
    with open(path, "a+") as f:
        f.write(f"\n{password}")


if __name__ == '__main__':
    print('u cant run this file as main')
