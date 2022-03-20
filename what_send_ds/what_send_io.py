import pathlib
from what_send_ds.what_send_logic import add_new_path, whole_path_list, choose_the_path
pass_ways = pathlib.Path(__file__).parent / 'pass_ways.txt'


def what_send_ds_io(text_path: str):

    path = text_path

    add_new_path(pass_ways, path)

    whole_path_list(pass_ways)
    print("Choose which file should bot send (write a number next to the path)")

    what_we_need = int(input())

    return choose_the_path(pass_ways, what_we_need)
