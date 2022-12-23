# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

from dataclasses import dataclass
from pathlib import Path

@dataclass
class InputData:
    command: str = None
    path: Path = None
    edit: str = None
    prnt: str = None
    param: str = None

INTRO = "\tWelcome to the ICS32 Distributed Socail Profile Interface!"
INVALID = 'ERROR, invalid input'

OPEN_PROFILE = "Do you have a profile or would you like to create one? (1: Load your profile, 2: Create a profile, 3: Quit program)\n"
PATH = 'Where is your profile file located?\n'
PLACE = "Where would you like to save your profile file?\n"
NEW_PROFILE = "Enter the name for your profile file:\n"

OPTIONS = "What would you like to do? Please select one of the options:"
LIST_COMMANDS = " 1: Print profile data\n 2: Publish a post\n 3: Edit your profile\n 4: Logout\n"

EDIT = "Please select an option for your profile:"
EDIT_OPTIONS = "  1: Add a new post\n  2: Change your username\n  3: Change your password\n  4: Change your Bio"
edit = {"2": "usr", "1": "add", "3": "pwd", "4": "bio"}
E_USR = "Enter your new username:\n"
E_PWD = "Enter you new password:\n"
E_BIO = "Enter your new bio:\n"
NEW_POST = "Enter your new post:\n"

PUB_POST = "Enter the ID of the post you want to publish: "

PRINT = "Please select an option to print:"
PRINT_OPTIONS = "  1: Print your Username\n  2: Print your Password\n  3: Print your Bio\n  4: Print your post history\n  5: Print everything from Profile"
prnt = {"1": "usr", "2": "pwd", "3": "bio", "4": "posts", "5": "all"}


def load_profile():
    select = input(OPEN_PROFILE)
    return select


def interact_profile():
    user_data = InputData()
    print(OPTIONS)
    select = input(LIST_COMMANDS)

    user_data.command = select

    if select == '3': # user selects edit
        print(EDIT)
        print(EDIT_OPTIONS)
        select = input() # ask for edit
        while select not in ['1', '2']:
            print(INVALID)
            select = input()
        if select == '1':
            user_data.edit = edit[select]
            #select = input(NEW_POST)
            #user_data.param = select
        elif select == '2':
            user_data.edit = edit[select]
            select = input(E_USR) # ask for new username
            user_data.param = select
        elif select == '3':
            user_data.edit = edit[select]
            select = input(E_PWD) # ask for new password
            user_data.param = select
        elif select == '4':
            user_data.edit = edit[select]
            select = input(E_BIO) # ask for new bio
            user_data.param = select
            
    elif select == '2': # user selects publish
        select = input(PUB_POST) # ask for post id
        user_data.param = select

    elif select == '1':
        print(PRINT)
        print(PRINT_OPTIONS)
        select = input() # ask for print
        while select not in [str(i) for i in range(6)]:
            print(INVALID)
            select = input()
        user_data.prnt = prnt[select]
        
    elif select == '4':
        return '4'
    
    else:
        print(INVALID)
    
    return user_data

if __name__ == '__main__':
    print(interact_profile())
