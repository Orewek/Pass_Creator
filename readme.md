# Pass creator
## Usage
Install with `pip install -r requirements.txt`
## Explanation how it works on user-level
### For programmer
* User type `the length` of the new password
* User types the `tag`. It will help to find the exact password in `.txt` later
* User can remove `_ , -, lower, upper, digits` from the password
* To easier learn this password user gets the learn_code 
* User can add some `comments` to the password
* Program saves into exact `pass.txt` that user wants (as the `default` `C:\passwords.txt`)
* Bot can `send` this `txt` file into the `discord`, if user will type a command for that


### For user 
* Write a `length` that u want for your password
* Write for what u will use it. It will help u to find the exact password that u looking for just by CTRL + F
* Remove `- _` from your password if u need to
* Learn your password, program will show u a words which will help you in that
* Add some `comments` to your password, it can help you, if you have a few accounts in 1 place (steam, for example)
* Save this password into the exact `pass.txt` that u want
* U can send this file to discord channel by the bot (it will sends `.txt` into the chat)


## Documentation

#### Methods
* `main` - main, the core of the program
* `remove_excess_password_io` - 1st: removes `_ -` 2nd: removes `lower, upper, digits` from the password
    * `tune_special_symbols` - logic part for the `1st` one
    * `sanitize_password` - logic part for the `2nd` one
* `comments_to_password_io` - add comments to the password
    * `add_comments` - logic part
* `learn_io` - learn_code to easier learn the password
    * `learn_logic` - logic part
* `save_into_txt_io` - save in `exact` `file.txt` that u want
    * `default_save` - `default` save into `C:\passwords.txt`
    * `user_path_save` - save into user `file.txt`
* `what_send_ds_io` - choose `wheres to save` your password and `which file` bot should `send` to you
    * `add_new_path` - add a new path to `pass_ways.txt`. After that u `can choose` form this list `exact` file
    * `whole_path_list` - just showing this `list with whole paths` into it
    * `choose_the_path` - user choose `exact` file that bot should send into the chat
* `on_ready` - start up the `discord bot`
* `on_message` - sends `.txt file` with passwords to `discord`

#### Fun's explanation
##### tune_special_symbols
```py
chars = '- _'
for char in chars:
        password = password.replace(char, '')
    return password

password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O'
password_without_underscore_and_dash = '63fFZ6wUnjCfDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O'
```
##### sanitize_password
```py
types = 'lowdig'
if 'up' in types:
    password = password.lower()
if 'low' in types:
    password = password.upper()
if 'dig' in types:
    password = ''.join([i for i in password if not i.isdigit()])
return password

password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O'
password_without_digits_and_lower = 'FFZ-WUNJ_C_FDSFFVQETUMKGDAQPANRLNLBVZIBALDUSYJO'
```
##### learn_password
```py
'a': 'apple',
'b': 'bestbuy',
'c': 'coffee',
...
'z': 'zip',

res = ''

for i in range(len(password)):
    res += f'{switcher[password[i]]} '

return res.strip()

password = 'vmLh3Det'
learn_code = 'visa music LAPTOP hulu 3 DRIP egg tokyo'
```
##### add_comments
```py
data = ' // '
    creation_date = datetime.datetime.now()
    if '-time' in comment:
        comment = comment.replace('-time', '')
        data += f'creation date - {creation_date}' + ' // '

    if '-len' in comment:
        comment = comment.replace('-len', '')
        data += f'length - {len(password)}'

    password += ' ' + comment + data

    return password
password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'
comment = 'barak -lenobama' #also it can be 'barak obama-len' 'barak obama -len' etc
password_with_comment = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3 barak obama // length - 30'
```
##### save_logic.user_path
```py
def default_save(password: str, default_path: str):
    """adding a new password to the file"""
    with open(default_path, "a+") as f:
        f.write(f"\n{password.strip()}")


def user_path_save(password: str, txt_path: str):
    """adding a new password to a user-path file"""
    path = rf'{txt_path}'
    with open(path, "a+") as f:
        f.write(f"\n{password}")
```
##### what_send_logic
```py
pass_ways = pathlib.Path(__file__).parent / 'pass_ways.txt'


def add_new_path(file_path: str, path: str):
    """Add a path entry to a text file. If the path already exists do nothing."""
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
        for count, re in enumerate(res):
            print(count, re)


def choose_the_path(pass_ways: str, what_we_need: int):
    """
    return a exact path that user want
    pass_ways - file.txt with whole ways to passwords.txt (user can make a few)
    """
    with open(pass_ways, 'r') as f:
        res = f.read().splitlines()

        for count, re in enumerate(res):
            if count == what_we_need:
                return re
```
##### discord bot
```py
client = discord.Client()


@client.event
async def on_ready():
    # waiting when bot will log into discord
    print('We have logged in as {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        # waiting when user will type smth in chat
        return

    path = r"D:\passwords.txt"
    if (True):
        # sending .txt with our passwords
        await message.channel.send(file=discord.File(path))

client.run(ds_token)
```
## Release History
* 0.5.1
    * Now User can do only a few steps (for example add a comment) for `already` created password
    * Project restructuring 
    * Making a 80 symbols line code
    * Add more type checks and fix a bug about `txt_path` save
* 0.5.0
    * Add a `learn_password`, now user can easier learn it. For example `a - apple, U - USA`
    * More `__doc__`'s  for god of docs
* 0.4.1
    * Now u can choose which `txt` file bot sends to u
* 0.4.0 
    * Now user can save `pass.txt` in exact file that he wants (only need to write a way to this file)
    * Now if user didnt use special command for `comments` (as `-len`) password will not contain `//` 
* 0.3.0
    * Add `readme.md` and `requirements.txt`
    
* 0.2.2
    * Add `param` for comments. `-len`: length of the pass, `-time`: creation date
    * Add `__doc__` to whole `funs` into the code
* 0.2.0.1
    * Add a folders for `io` and `logic`
    * Add `comments` to the password and 1 `unitTest` for that
* 0.2.0
    * Add `discord bot` and `.env` to `.gitigrone`
* 0.1.3
    * separate `funs` to `logic` and `io`
* 0.1.2
    * Add `unitTests` and `__name == '__main__'` for whole files
* 0.1.1
    * Add `.gitignore` and `comments` for some funs and `main()`
* 0.1.0
    * Initial release
