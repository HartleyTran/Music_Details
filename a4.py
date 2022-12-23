# a4.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

import OpenWeather, LastFM, ui, ds_client
import ExtraCreditAPI as EC
from ExtraCreditAPI import ExtraCredit
from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI
from Profile import DsuFileError, Profile, Post
from pathlib import Path

OW_API = "cc59bfa134d7ea5f1e1abecb1c7087e4"
FM_API = "34e6c5af26bbc7656c1215d06e09e517"
dsu_path = ''
server = "168.235.86.101" 
port = 3021

def transclude(message:str, webapi:WebAPI):
    """
    Loads API data and API's tranclusion is done on the message
    """
    webapi.load_data()
    result = webapi.transclude(message)
    return result


def main():
    """
    Instantiates APIs and sets each APIs' apikey. Asks user for a message then transcludes any keywords in the message. Returns transcluded message

    """
    ow_obj = OpenWeather(92626, 'US')
    ow_obj.set_apikey(OW_API)

    fm_obj = LastFM()
    fm_obj.set_apikey(FM_API)

    ec_obj = ExtraCredit()
    ec_obj.set_apikey(EC.EXTRACREDITAPIKEY)

    msg = input("Enter a message (Keywords: @weather, @lastfm, @extracredit):\n")
    msg = transclude(msg, ow_obj)
    msg = transclude(msg, fm_obj)
    msg = transclude(msg, ec_obj)

    return msg


def open_profile(inpt):
    """
    Opens or Creates a profile based on the user input
    """#C:\Users\hartl\OneDrive\Desktop\a2
    global dsu_path, server

    if inpt == '2': # creates a new profile, if profile already exists it loads that profile
        dsu_path = input(ui.PLACE) + '\\' + input(ui.NEW_PROFILE) + '.dsu'        
        p = Path(dsu_path)
        if not p.exists():
            p.touch()
            print('Profile created at:', dsu_path)

            server = input('Enter the server IP Address: ')
            username = input('Enter your username: ')
            password = input('Enter a password: ')
            bio = input('Enter a bio: ')

            user = Profile(server, username, password)
            user.bio = bio
            user.save_profile(dsu_path)
        else:
            print('Profile already exists')
            user = Profile()
            user.load_profile(dsu_path)
            print('Loading profile...')
            print('\tUsername:', user.username)
            print('\tPassword:', user.password)
            print('\tBio:', user.bio)

    if inpt == '1': # opens an existing profile
        dsu_path = input(ui.PATH)
        p = Path(dsu_path)   
        while not p.exists() or dsu_path[-4:] != '.dsu':
            print('Profile does not exist')
            dsu_path = input(ui.PATH)
            p = Path(dsu_path)
        
        user = Profile()
        user.load_profile(dsu_path)
        print('Loading profile...')
        print('\tUsername:', user.username)
        print('\tPassword:', user.password)
        print('\tBio:', user.bio)



def operate():
    """
    After creating or loading a profile, the user can edit/print aspects of their profile info, publish a post, or logout of their profile
    """
    global dsu_path, server

    if usr_input.command == '3': #edits profile
        if not dsu_path:
            print("No profile loaded") 
        else:
            user = Profile()
            user.load_profile(dsu_path)

            if usr_input.edit == 'bio':
                inpt2 = usr_input.param
                user.bio = inpt2
                ds_client.send(user.dsuserver, port, user.username, user.password, '', user.bio)

            elif usr_input.edit == 'add':
                inpt2 = main() 
                post = Post()
                post.entry = inpt2
                user.add_post(post)

            user.save_profile(dsu_path)

    if usr_input.command == '2': #publishes a post
        if not dsu_path:
            print("No profile loaded")
        else:
            user = Profile()
            user.load_profile(dsu_path)

            posts = user.get_posts()
            opt_inpt = int(usr_input.param)
            post = posts[opt_inpt]
            entry = post.get_entry()
            ds_client.send(user.dsuserver, port, user.username, user.password, entry, user.bio)

    if usr_input.command == "1": #print profile
        if not dsu_path:
            print("No profile loaded")
        else:
            user = Profile()
            user.load_profile(dsu_path)
            if usr_input.prnt == 'usr':
                print(user.username)

            elif usr_input.prnt == 'pwd':
                print(user.password)

            elif usr_input.prnt == 'bio':
                print(user.bio)

            elif usr_input.prnt == 'posts':
                posts = user.get_posts()
                print("Post History:")
                for i in range(len(posts)):
                    print(f' [{i}] {posts[i].get_entry()}')

            elif usr_input.prnt == 'all':
                print('Username:', user.username)
                print('Password:', user.password)
                print('Bio:', user.bio)
                print('Post(s):')
                posts = user.get_posts()
                for i in range(len(posts)):
                    print(f'[{i}] {posts[i].get_entry()}')


if __name__ == '__main__':
    print(ui.INTRO)
    usr_input = ui.load_profile()
    while usr_input not in ['1', '2', '3']: # creates loop if user inputs invalid cmd
        print(ui.INVALID)
        usr_input = ui.load_profile()
    
    while usr_input != '3':
        open_profile(usr_input)
        usr_input = ui.interact_profile()
        while usr_input != '4':
            operate()
            usr_input = ui.interact_profile()
        usr_input = ui.load_profile()
else:
    ds_client.send(server, port, 'person1001', 'abc123', 'hello')