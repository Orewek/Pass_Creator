import pathlib

from what_send_ds.what_send_logic import add_new_path, choose_the_path, whole_path_list
pass_ways = pathlib.Path(__file__).parent / 'pass_ways.txt'


def what_send_ds_io(text_path: str) -> str:
    # path that user choosed to save
    path = text_path

    # if path not in our path-list, add that
    add_new_path(pass_ways, path)

    # printing the whole numerated path-list
    whole_path_list(pass_ways)

    # user choosing which file should bot send into the discord
    what_we_need = int(input("Choose which file should bot send (write a number next to the path)"))

    return choose_the_path(pass_ways, what_we_need)
