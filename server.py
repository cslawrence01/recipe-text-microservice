
import zmq
import re


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")


while True:

    byte_str = socket.recv()

    string_decoded = byte_str.decode("utf-8")

    # extract the title from the string
    pattern = '^(.+):'
    match = re.search(pattern, string_decoded)
    title = match.group(1)
    title = title + ".txt"
    file_name = title # the filename will just be the title of the recipe


    # open the text file for writing
    with open(file_name, 'w') as f:
        f.write(string_decoded)

    #  Send reply back to client
    socket.send(b"file saved successfully")

    break



