import urllib, json
from urllib import request, error
import time
from WebAPI import WebAPI

class OpenWeather(WebAPI):
    temperature = None
    high_temperature = None
    low_temperature = None
    longitude = None
    latitude = None
    description = None
    humidity = None
    city = None
    sunset = None

    def __init__(self, zipcode:str = '92697', location:str = 'US'):
        self.location = location
        self.zipcode = zipcode


    def _download_url(self, url: str) -> dict:
        return super()._download_url(url)


    def set_apikey(self, apikey: str) -> None:
        return super().set_apikey(apikey)


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
	
        '''
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.location}&appid={self.apikey}"
        
        weather_obj = self._download_url(url)

        try:
            self.temperature = weather_obj['main']['temp']
            self.high_temperature = weather_obj['main']['temp_max']
            self.low_temperature = weather_obj['main']['temp_min']
            self.longitude = weather_obj['coord']['lon']
            self.latitude = weather_obj['coord']['lat']
            self.description = weather_obj['weather'][0]['description']
            self.humidity = weather_obj['main']['humidity']
            self.city = weather_obj['name']
            sec = weather_obj['sys']['sunset']
            self.sunset = time.strftime("%H:%M:%S", time.localtime(sec))
        except TypeError:
            print('Invalid URL loaded')
    

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
	
        :returns: The transcluded message
        '''
    
        if '@weather' in message:
            # change display_msg to desired data to display
            display_msg = self.city
            new_msg = message.replace('@weather', str(display_msg))
            return new_msg
        else:
            return message

if __name__ == '__main__':
    zipcode = "92697"
    ccode = "US"
    apikey = "cc59bfa134d7ea5f1e1abecb1c7087e4"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    # change test_msg to test if transclude function correctly replaces @weather keyword to a data value
    test_msg = "The weather is looking like @weather right now."
    print(open_weather.transclude(test_msg))
