import socket
import struct
import select

NOP = 0
LEFT = 1
RIGHT = 2
QUIT = 3

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
        self.c.setblocking(0)
        print("Socket running with connection from ", self.addr)

    def get_data(self):
        recieve = self.c.recv(1024)
        print(recieve)
        if recieve == b'1':
            self.data = -1
        if recieve == b'0':
            self.data = 1
        else:
            self.data = 0

        readable, writable, exceptional = select.select([self.c], [], [self.c], 0)

        if self.c in readable:
            receive_str = self.c.recv(1024)

            if recieve_str:
                command = struct.unpack('i', recieve_str)[0]
                print('command: {}'.format(command))
                if command == LEFT:
                    self.data = -1

                elif command == RIGHT:
                    self.data = 1
