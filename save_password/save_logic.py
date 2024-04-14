def default_save(password: str, default_path: str) -> None:
    """
    adding a new password to the default path file
    default_path = r'C:[back slash]passwords.txt'
    """
    with open(default_path, "a+") as f:
        lines = f.readlines()
        if len(lines) == 0:
            f.write(f"{password}\n")
        elif lines[-1].endswith("\n"):
            f.write(f"{password}\n")
        else:
            f.write(f"\n{password}")


def user_path_save(password: str, txt_path: str) -> None:
    """adding a new password to a user-path file"""
    path = rf'{txt_path}'
    with open(path, "a+") as f:
        lines = f.readlines()
        if len(lines) == 0:
            f.write(f"{password}\n")

        elif lines[-1].endswith("\n"):
            f.write(f"{password}\n")

        else:
            f.write(f"\n{password}")


if __name__ == '__main__':
    print('u cant run this file as main')
