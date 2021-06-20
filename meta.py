import os
import platform


def cls():
    user_os = platform.system().lower()
    if user_os == "windows":
        os.system('cls')
    elif user_os == "linux" or user_os == "macos":
        os.system('clear')
    else:
        print("OS Not Found !")


def ask_yes_no(text_input):
    while True:
        use_pass = input(text_input).lower()
        if use_pass == "y" or use_pass == "n":
            return use_pass
        else:
            print("Your Answer is not recognized")
            print("You must type 'y' or 'n'")
            continue
