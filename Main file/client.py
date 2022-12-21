from websocket import create_connection
from threading import Thread
import json
from cThread import StoppableThread
import sys


clientID = '85'
username = "Shivam"

ws = create_connection("wss://concord-28ll.onrender.com/api/v1/chats/all/ws/"+clientID)

def read():
    alive = True
    while(alive):
        try: 
            print("Server ", ws.recv())
        except (KeyboardInterrupt, SystemExit,  EOFError):
            alive = False
            print("Exiting read")


def write():
    alive = True
    while(alive):
        try: 
            inp = input(">> ")
            mes = {"username": username, "message": inp}
            ws.send(json.dumps(mes))
        except (KeyboardInterrupt, SystemExit, EOFError):
            print("Exiting write")
            alive = False

readThread = StoppableThread(target=read)
writeThread = StoppableThread(target=write)
    
try:
    readThread.start()
    writeThread.start()
except (KeyboardInterrupt, SystemExit):
    readThread.stop()
    writeThread.stop()
    sys.exit()
    




