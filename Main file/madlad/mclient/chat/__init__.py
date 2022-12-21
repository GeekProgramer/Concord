from websocket import create_connection
from threading import Thread
import json
from cThread import StoppableThread
import sys


class ChatManager:
    def __init__(self, clientID):
        self.onMes = None
        self.ws = create_connection("wss://concord-28ll.onrender.com/api/v1/chats/all/ws/" + clientID)
        readThread = StoppableThread(target=self.read)
        readThread.start()
        # writeThread = StoppableThread(target=self.write)

    def read(self):
        alive = True
        while alive:
            try:
                mes = self.ws.recv()
                jsonMes = json.loads(mes)
                if self.onMes is not None:
                    self.onMes(jsonMes["username"], jsonMes["message"])
                print("Server ", mes)
            except:
                alive = False
                print("Exiting read")

    def onMessage(self, fn):
        self.onMes = fn

    def sendMessage(self, username, message):
        mes = {"username": username, "message": message}
        try:
            self.ws.send(json.dumps(mes))
        except:
            print("Something went wrong bruh")