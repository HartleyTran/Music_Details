# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

#https://www.balldontlie.io/api/v1/teams

import urllib, json
from urllib import request,error
import random
from WebAPI import WebAPI

class ExtraCredit(WebAPI):
    name = None
    height = None
    position = None
    team = None
    weight = None

    def _download_url(self, url: str) -> dict:
        return super()._download_url(url)


    def set_apikey(self, apikey: str='') -> None:
        return super().set_apikey(apikey)


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
	
        '''
        id = random.randint(1,2000)
        url = f"https://www.balldontlie.io/api/v1/players/{id}"
        
        player_obj = self._download_url(url)

        if player_obj is not None:
            self.name = f"{player_obj['first_name']} {player_obj['last_name']}"
            self.height = 'NA' if not player_obj['height_feet'] else f"{player_obj['height_feet']}\' {player_obj['height_inches']}\""
            self.position = 'NA' if not player_obj['position'] else player_obj['position']
            self.team = player_obj['team']['full_name']
            self.weight = 'NA' if not player_obj['weight_pounds'] else player_obj['weight_pounds']

    

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
	
        :returns: The transcluded message
        '''
        #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        if '@extracredit' in message:
            insert_msg = f'{self.name} from the {self.team}'
            new_msg = message.replace('@extracredit', insert_msg)
            return new_msg
        else:
            return message
      
EXTRACREDITAPIKEY = ""

if __name__ == '__main__':
    player = ExtraCredit()
    player.set_apikey(EXTRACREDITAPIKEY)
    player.load_data()

    print(player.transclude('My favorite player is @extracredit'))
    print(player.apikey)
