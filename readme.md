# Pass creator
## Usage
Install with `pip install -r requirements.txt`
## Explanation how it works on user-level
### For programmer
* User type `the length` of the new password
* User types the `tag`. It will help to find the exact password in `.txt` later
* User can remove `_ , -, lower, upper, digits` from the password
* User can add some `comments` to the password
* Program saves it in `pass.txt`
* Bot can `send` this `txt` file into the `discord`, if user will type a command for that

### For user 
* Write a `length` that u want for your password
* Write for what u will use it. It will help u to find the exact password that u looking for just by CTRL + F
* Remove `- _` from your password if u need to
* Add some `comments` to your password, it can help you, if you have a few accounts in 1 place (steam, for example)
* Save this password to your `pass.txt`
* U can send this file to discord channel by the bot (it will sends `.txt` into the chat)


## Documentation

#### Methods
* `main` - main, the core of the program
* `remove_excess_password_io` - 1st: removes `_ -` 2nd: removes `lower, upper, digits` from the password
    * `tune_special_symbols` - logic part for the `1st` one
    * `sanitize_password` - logic part for the `2nd` one
* `comments_to_password_io` - add comments to the password
    * `add_comments` - logic part
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
* 0.3.0.1 Add fun's code, more explanation as for programmers and as for users into `readme.md`
* 0.3.0 - Add `readme.md` and `requirements.txt`
* 0.2.3.1 - Minor fixes
* 0.2.3 - Add `__doc__` to whole `funs` into the code
* 0.2.2 - Add `param` for comments. `-len`: length of the pass, `-time`: creation date
* 0.2.1 - Add `comments` to the password and 1 `unitTest` for that
* 0.2.0.1 - Add a folders for `io` and `logic`
* 0.2.0 - Add `discord bot` and `.env` to `.gitigrone`
* 0.1.4 - separate `funs` to `logic` and `io`
* 0.1.3.1 - Make `avto` `unitTests` user dont need to write `test` or smth else for that
* 0.1.3 - Add `unitTests` and `__name == '__main__` for whole files
* 0.1.2 - Add comments for some funs and `main()`
* 0.1.1 - Add `.gitignore`
* 0.1.0 - Initial release
