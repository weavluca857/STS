# Run instructions

## Python version
3.9.1

## Install all the necessary packages

1. pygame 
    
    `pip3 install pygame -U`
2. keyboard

    `pip3 install keyboard`
3. Circuitpy 
   
    Follow the directions in circuitpy.md

## Run pong game

    python3 pong.py

If Multiplayer is desired, when clicking on the option for multiplayer, open up a new terminal to ~/STS/Drivers and run `python3 socket_client.py`

## Common Errors

When running the game you may have a problem with pygame instantiating a video driver. This can be solved by running it on a vm. It should work for windows 10 as that is the development environment.
