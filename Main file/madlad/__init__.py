from .mclient import auth
from .mclient import chat


class Madlad:
    def __init__(self):
        pass

    def login(self, username, password):
        return auth.login(username, password)

    def register(self, username, password):
        return auth.register(username, password)

    def getChatManager(self):
        return chat.ChatManager


# client = madlad()
# response =  client.login("Saurav", "444")
# client.register("Shivam", "123")