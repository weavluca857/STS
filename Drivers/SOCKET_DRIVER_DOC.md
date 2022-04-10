# Socket Driver Doc

## Imports
1. socket

    Link to documentation: https://docs.python.org/3/library/socket.html

## Classes

### Server

#### Variables

1. `HOST`

   Contains the host address for the server
2. `PORT`

   Contains the port in which it will be listening
3. `data`

   Contains the data that is recieved from the client
4. `s`

   Contains the socket container

#### Functions

1. `__init__(self, s)`

   1. `s` contains the socket container

   This initializes the server which will recieve the data from other players
2. `listen(self)`

   This will wait for a connection to the server to be established
3. `get_data(self)`

   This will receive the data and determine which direction it corresponds to

## Future work

1. Debug closing the server socket too soon. 
2. Fix overall mechanics to work better