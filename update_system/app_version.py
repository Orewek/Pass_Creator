import pandas as pd


def check_version() -> None:

    app_version: int = 51

    current_git_version_link: str = 'https://raw.githubusercontent.com/Orewek/Pass_Creator/master/update_system/github_version.csv'

    get_git_version = pd.read_csv(current_git_version_link)
    current_git_version = get_git_version['version'][0]
 
    if current_git_version > app_version:

        txt: str = input(""" 
                         A new version has came out! Do u want to get it? Your whole files was already saved for this update!
                         Do u want to get it? Y/N
                         """)
        if txt.lower() == 'y':
            $git clone https://github.com/Orewek/Pass_Creator.git

            with open(r'D:\imp_passwords.txt') as f:
                s = f.readlines()
                mas: list = []
                for i in range(len(s)):
                    mas.append(s[i])


            with open(r'C:\Users\D.Charykov\!prog\vscode\Pass_creator\what_send_ds\pass_ways.txt', 'w') as ff:
                for i in range(len(mas)):
                    ff.write(mas[i])

        app_version: int = get_git_version['version'][0]

        print('Newer version was succesfully installed')



