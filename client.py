#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to the text service server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# here the main application will put in the correct parameters
request_dict = {
    "recipe-string": "string",
    "dir": "./<dir_name>/",
    "alignment": "center",
    "other params": "value"
}

# convert to json
request_json = json.dumps(request_dict)

# send to server
socket.send(request_json)




"""
#  Do 10 requests, waiting each time for a response
for request in range(1):
    print(f"Sending request {request} …")
    msg_to_send = b"A message from CS361"
    print(f"sending: {msg_to_send}")
    socket.send(msg_to_send)

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
    
"""
