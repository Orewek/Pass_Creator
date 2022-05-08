''' user will able to change smth on each stage'''
'''
def change_check(user_input: str):
    if user_input == '-change' and in change_str:
        res = change_str.strip().split(' ')
        for count, item in enumerate(res):
            print(count, item)

        change_it()
    if user_input == '-change' and not in change_str:
        print('U cant change rn! complete this input')


def change_it():
    print('fuck yeah!')

change_str = 'password_length tag tag_password password_wo_slash_underscore comment_password txt_path res_path'

def main():
    password_length = input()
    tag = str(input())
    tag_password = tag + "_" + secrets.token_urlsafe(3 * password_length)
    password_wo_slash_underscore = remove_excess_password_io(tag_password)[:password_length]
    comment_password = comments_to_password_io(password_wo_slash_underscore)
    txt_path = save_into_txt_io(comment_password)
    res_path = what_send_ds_io(txt_path)
    bot(res_path)

'''
