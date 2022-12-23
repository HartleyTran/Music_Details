from abc import ABC, abstractmethod
import urllib, json
from urllib import request, error

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    """
    Opens the HTTP url and receives the response from the API
    Returns the response as a JSON dict if successful else informs user of error

    """
    response = None
    r_obj = None

    try:
      response = urllib.request.urlopen(url)
      json_results = response.read()
      r_obj = json.loads(json_results)

    except error.HTTPError as e:
      print('Failed to download contents of URL')
      print('Status code: {}'.format(e.code))
        
    except error.URLError as e:
      print('Failed to download contents of URL')
      print('Loss connection to Internet')

    finally:
      if response != None:
        response.close()
    
        return r_obj
	

  def set_apikey(self, apikey:str) -> None:
    '''
    Sets the apikey required to make requests to a web API.
    :param apikey: The apikey supplied by the API service
    
    '''
    self.apikey = apikey
	
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
