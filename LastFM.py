# lastfm.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

import urllib, json
from urllib import request, error
import time
from WebAPI import WebAPI

class LastFM(WebAPI):
    track_name = None
    track_artist = None
    track_album = None
    last_played = None
    currently_playing = False

    def __init__(self, username:str = 'hartlehar'):
        self.username = username


    def _download_url(self, url: str) -> dict:
        return super()._download_url(url)


    def set_apikey(self, apikey: str) -> None:
        return super().set_apikey(apikey)


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
	
        '''
        url = f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={self.username}&api_key={self.apikey}&limit=10&format=json"
        
        track_obj = self._download_url(url)

        if track_obj is not None:
            self.track_artist = track_obj['recenttracks']['track'][0]['artist']['#text']
            self.track_name = track_obj['recenttracks']['track'][0]['name']
            self.track_album = track_obj['recenttracks']['track'][0]['album']['#text']

            if '@attr' in track_obj['recenttracks']['track'][0]:
                self.currently_playing = track_obj['recenttracks']['track'][0]['@attr']['nowplaying']
            
            if 'date' in track_obj['recenttracks']['track'][0]:
                self.last_played = track_obj['recenttracks']['track'][0]['date']['#text']
    

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
	
        :returns: The transcluded message
        '''
        #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        if '@lastfm' in message:
            insert_msg = f'"{self.track_name}" by {self.track_artist}'
            new_msg = message.replace('@lastfm', insert_msg)
            return new_msg
        else:
            return message

if __name__ == "__main__":
    username = "hartlehar"
    apikey = "027e11ae05538b168c60e66ef478eec6"

    last_fm = LastFM()
    last_fm.set_apikey(apikey)
    last_fm.load_data()
    print(last_fm.transclude("I am listening to @lastfm."))
