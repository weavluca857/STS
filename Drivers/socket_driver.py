import socket

class Server:

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    data = 0

    def __init__(self, s):
        self.s = s
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()

    def listen(self):
        self.c, self.addr = self.s.accept()
        print("Socket running with connection from ", self.addr)

    def get_data(self):
        recieve = self.c.recv(1024)
        print(recieve)
        if recieve == b'1':
            self.data = -1
        if recieve == b'0':
            self.data = 1
