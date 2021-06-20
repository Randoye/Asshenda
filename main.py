# Python Files Import
import ssh
import meta
from db import fetch_last_ip, condb, initdb
# PIP Import
import os
pwd = os.getcwd()
last_ip_con = None


def mainmenu():
    last_ip = fetch_last_ip()
    print("====================================")
    print("Welcome to the main menu")
    print("What do you want to do ?")
    if last_ip:
        print(f"0: Connect to the most recent SSH ({last_ip})")
    print("1: Launch an SSH Connection")
    print("2: Add a new SSH Connection")
    print("3: Delete an SSH Connection")
    print("5: Exit the program")
    print("\n")
    input_menu = input(" What do you want to do (Type the number) ? ")
    return input_menu


if __name__ == '__main__':
    meta.cls()
    print("Welcome to SSHClient !")
    while True:
        db = condb()
        initdb(db)
        input_main = mainmenu()
        try:
            input_main = int(input_main)
        except:
            print("Please use a number !")
        if input_main == 1:
            ssh.showallssh()
            ssh.sshcon()
        elif input_main == 2:
            ssh.addssh()
        elif input_main == 5:
            raise SystemExit
        else:
            print("Your Answer is not recognized")
