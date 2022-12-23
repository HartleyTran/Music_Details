# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

import json
from collections import namedtuple
from tempfile import tempdir

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['cmd', 'token', 'resp'])
temp = []

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    global temp
    temp = []
    json_obj = json.loads(json_msg)
    if "response" in json_obj:
      if json_obj["response"]["type"] == 'ok':
        data = DataTuple('O', json_obj["response"]["token"] if 'token' in json_obj["response"] else '', json_obj["response"]["message"])
      elif json_obj["response"]["type"] == 'error':
        data = DataTuple('E', '', json_obj["response"]["message"])
      
    elif "join" in json_obj:
      if json_obj["response"]["type"] == 'ok':
        data = DataTuple('O', json_obj["response"]["token"] if 'token' in json_obj["response"] else '', json_obj["response"]["message"])
      elif json_obj["response"]["type"] == 'error':
        data = DataTuple('E', '', json_obj["response"]["message"])
    
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return data


def unwrap(dic):
  '''
  Creates a list of the elements in json_obj
  '''
  global temp
  for i in dic:
    if type(dic[i]) == dict:
      temp.append(i)
      unwrap(dic[i])
    else:
      temp.append(dic[i])
  
  return temp