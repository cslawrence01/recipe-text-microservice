
import time
import zmq
import re


context = zmq.Context()
socket = context.socket(zmq.REP)
#socket.bind("tcp://*:6666")
socket.bind("tcp://*:5555")
print("server initialized")

while True:
    #  Wait for next request from client

    # receive json object
    byte_str = socket.recv()


    string_decoded = byte_str.decode("utf-8")
    print(f"micro service prints byte string: {string_decoded}")

    pattern = '^(.+):'
    match = re.search(pattern, string_decoded)
    title = match.group(1)
    print(title)
    title = title + ".txt"
    print(title)
    file_name = title # the filename will just be the title
    #file_name = "./" + file_name

    # open the text file for writing
    with open(file_name, 'w') as f:
        ######
        # apply string transformation here to fit customization
        ####3#
        f.write(string_decoded)

    # write success/error message here, back to client log file
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"file saved successfully")

    break



