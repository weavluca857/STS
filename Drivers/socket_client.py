# echo-client.py

import socket
#import keyboard
import struct
import curses


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

"""
while 1:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        s.send(b'1')
    if event.event_type == keyboard.KEY_DOWN and event.name == 'e':
        s.send(b'0')
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
        s.send(b'')
        break
"""

NOP = 0
LEFT = 1
RIGHT = 2
QUIT = 3

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()

event_enum = NOP

try:
    while event_enum != QUIT:

        event_enum = NOP
        ch = stdscr.getch()

        if ch == ord('w'):
            event_enum = LEFT
        if ch == ord('e'):
            event_enum = RIGHT
        if ch == ord('q'):
            event_enum = QUIT

finally:
    curses.nobreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    s.close()

