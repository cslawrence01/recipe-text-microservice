#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client

    # receive json object
    json_obj = socket.recv()
    # convert back to python dictionary
    dict_obj = json.load(json_obj)
    print(f"Received request: {dict_obj}")

    # save file name with directory in a variable
    file_name = dict_obj.dir

    # open the text file for writing
    with open(file_name, 'w'):
        ######
        # apply string transformation here to fit customization
        ####3#
        file_name.write(dict_obj.recipe_string)

    # write success/error message here, back to client log file



    #  Do some 'work'
    #time.sleep(1)

    #  Send reply back to client
    #socket.send(b"A message from CS361")
