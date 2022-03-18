#Create a password
###### And send this to discord by the password bot

## Usage
Install with `pip install -r requirements.txt`

## Documentation

#### Methods
* `main` - main, the core of the program
* `remove_excess_password_io` - 1st: removes `_ -`, 2nd: removes `lower, upper, digits` from the password
    * `tune_special_symbols` - logic part for the `1st` one
    * `sanitize_password` - logic part for the `2nd` one
* `comments_to_password_io` - add comments to the password
    * `add_comments` - logic part
* `on_ready` - start up the `discord bot`
* `on_message` - sends `.txt file` to `discord`

## Release History
* 0.3.0 - Add `readme.md` and `requirements.txt`
* 0.2.3.1 - Minor fixes
* 0.2.3 - Add `__doc__` to whole `funs` into the code
* 0.2.2 - Add `param` for comments. `-len`: lenght of the pass, `-time`: creation date
* 0.2.1 - Add `comments` to the password and 1 `unitTest` for that
* 0.2.0.1 - Add a folders for `io` and `logic`
* 0.2.0 - Add `discord bot` and `.env` to `.gitigrone`
* 0.1.4 - separate `funs` to `logic` and `io`
* 0.1.3.1 - Make `avto` `unitTests` user dont need to write `test` or smth else for that
* 0.1.3 - Add `unitTests` and `__name == '__main__` for whole files
* 0.1.2 - Add comments for some funs and `main()`
* 0.1.1 - Add `.gitignore`
* 0.1.0 - Initial release
