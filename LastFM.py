import urllib, json
from urllib import request, error
import time
from WebAPI import WebAPI

class track:
    def __init__(self, name, artist, length) -> None:
        self.name = name
        self.artist = artist
        self.length = length
        

class LastFM(WebAPI):
    release_date = None
    album_name = None
    artist = None
    album_tracks = []
    album_length = None
    playcount = None
    total_duration = 0

    def __init__(self, username:str = 'hartlehar'):
        self.username = username


    def _download_url(self, url: str) -> dict:
        return super()._download_url(url)


    def set_apikey(self, apikey: str) -> None:
        return super().set_apikey(apikey)

    def set_album_name(self, name:str):
        self.album_name = name
    
    def set_artist(self, artist:str):
        self.artist = artist

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
	
        '''
        temp_name = self.album_name.replace(' ', '+')
        temp_artist = self.artist.replace(' ', '+')
        url = f"https://ws.audioscrobbler.com/2.0/?method=album.getInfo&api_key={self.apikey}&artist={temp_artist}&album={temp_name}&format=json"
        album_obj = self._download_url(url)
        
        if album_obj is not None:
            for t in album_obj['album']['tracks']['track']:
                self.album_tracks.append(track(t['name'], t['artist']['name'], t['duration']))
                self.total_duration += int(t['duration'])
        
        self.release_date = album_obj['album']['wiki']['published']
        self.playcount = album_obj['album']['playcount']
        self.album_length = len(self.album_tracks)

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
	
        :returns: The transcluded message
        '''
        if '@lastfm' in message:
            # change insert_msg to display desired information about album
            insert_msg = f'"{self.album_name}" has {self.album_length} songs and has been played {self.playcount} times'
            new_msg = message.replace('@lastfm', insert_msg)
            return new_msg
        else:
            return message

if __name__ == "__main__":
    username = "hartlehar"
    apikey = "027e11ae05538b168c60e66ef478eec6"


    last_fm = LastFM()
    last_fm.set_apikey(apikey)
    last_fm.set_album_name('The Forever Story')
    last_fm.set_artist('JID')
    last_fm.load_data()
    print(last_fm.album_length)
    print(last_fm.transclude("@lastfm."))
