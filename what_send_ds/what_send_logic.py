import pathlib
pass_ways = pathlib.Path(__file__).parent / 'pass_ways.txt'


def add_new_path(pass_ways, path):
    with open(pass_ways, "a+") as f:
        if str(path) not in str(pass_ways):
            f.write(f'\n{path}')


def whole_path_list(pass_ways):
    with open(pass_ways, 'r') as f:
        res = f.read().splitlines()
        for count, re in enumerate(res):
            print(count, re)


def choose_the_path(pass_ways, what_we_need: int):
    with open(pass_ways, 'r') as f:
        res = f.read().splitlines()
        for count, re in enumerate(res):
            if count == what_we_need:
                return re
