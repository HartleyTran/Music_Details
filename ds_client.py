# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Hartley Tran
# EMAIL: hartlemt@uci.edu
# STUDENT ID: 55747472

import socket
from sys import excepthook
from ds_protocol import extract_json
import json
import time

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))

      print(f'client connected to {server} on {port}')
      # creates JSON cmd for joining
      join_msg = {"join": {"username": username, "password": password, "token": ""}}
      join_msg = json.dumps(join_msg)
    
      send = client.makefile('w')
      recv = client.makefile('r')

      send.write(join_msg + '\r\n') # sends join JSON to server
      send.flush()

      resp = recv.readline()
      data = extract_json(resp)
      print(data.resp)
      token = data.token

      if data.cmd == 'O':
        if message: # create JSON cmd if message was inputed, sends to server, and prints response from server
          new_msg = {"token": token, "post": {"entry": message, "timestamp": str(time.time())}}
          new_msg = json.dumps(new_msg)

          send.write(new_msg + '\r')
          send.flush()

          resp = recv.readline()
          data = extract_json(resp)
          print(data.resp)
          if data.cmd == 'E':
            return False

        if bio: # create JSON cmd if bio was inputed, sends to server, and prints response from server
          new_bio = {"token": token, "bio": {"entry": bio, "timestamp": str(time.time())}}
          new_bio = json.dumps(new_bio)

          send.write(new_bio + '\r')
          send.flush()

          resp = recv.readline()
          data = extract_json(resp)
          print(data.resp)
          if data.cmd == 'E':
            return False
      elif data.cmd == 'E':
        return False
  except:
    print("Invalid port or IP")
    return False
    
  return True

"""
port = 3021
server = "127.0.0.1"
username = 'test_user'
password = 'abc1234567'
message = 'hello'
bio = 'my bio'

print(send(server, 2020, username, password, '', bio))
"""