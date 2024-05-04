import pathlib
pass_ways = pathlib.Path(__file__).parent / 'pass_ways.txt'


def add_new_path(file_path: str, path: str):
    """Add a path entry to a text file.
       If the path already exists do nothing."""
    with open(file_path, "a+") as file:
        file.seek(0)
        if path not in file.read().splitlines():
            file.write(f'\n{path.strip()}')


def whole_path_list(pass_ways: str):
    """
    numerate every path into the file
    pass_ways - file.txt with whole ways to passwords.txt (user can make a few)
    """
    with open(pass_ways, 'r') as f:
        res = f.read().splitlines()
        print(*[f'{count}: {item}' for count, item in enumerate(res)], sep='\n')


def choose_the_path(pass_ways: str, what_we_need: int):
    """
    return a exact path that user want
    pass_ways - file.txt with whole ways to passwords.txt
    (user can make a few .txt files with passwords)
    """
    with open(pass_ways, 'r') as f:
        res = f.read().splitlines()

        for count, item in enumerate(res):
            if count == what_we_need:
                return item


if __name__ == '__main__':
    print('U cant run this file as main')
