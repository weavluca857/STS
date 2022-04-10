# echo-client.py

import socket
import keyboard



HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while 1:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        s.send(b'1')
    if event.event_type == keyboard.KEY_DOWN and event.name == 'e':
        s.send(b'0')
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
        s.send(b'')
        break


s.close()