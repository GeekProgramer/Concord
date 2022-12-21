import socket
import threading
HOST=''
PORT=5555
LISTENER_LIMIT=5

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        server.bind((HOST,PORT))
    except:
        print("Error host and port")
    server.listen(LISTENER_LIMIT)

if __name__='__main__':
    