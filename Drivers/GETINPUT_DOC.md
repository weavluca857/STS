# GetInput Docs

## Imports

1. random 

    Link to Docs: https://docs.python.org/3/library/random.html
2. Driver.AIPADDLE

   Documentation found in AI_PADDLE_DOC.md
3. Driver.Connect

   Documentation found in CONNECT_DOC.md
4. Driver.SocketDriver

   Documentation found in SOCKET_DRIVER_DOC.md

## Classes

### gyro_data
Stores gyroscope information in a wrapper class.
#### Variables
1. `current_traj`
   
   Contains the information that will be output from the gyroscope sensor.
2. `MAX_X`

   Details the max sensitivity of the game on the X direction to determine paddle speed
3. `MAX_Y`

   Details the max sensitivity of the controller in the Y direction for paddle speed in game.
4. `MAX_Z`

   Details the max Z sensitivity of the gyroscope sensor. Not very applicable in this project.

#### Functions
1. `__init__(self)`

   Initializes the object with a `current_traj` of (0,0,0)
2. `set_data(self, x, y, z)`

   Sets `current_traj` to the values passed in by the argument variables

### LAN_output
Stores the output of the LAN communication in a way that is standard to output to the pong game. 
#### Variables 
1. `up` 

   This stores information on the movement of the paddle: -1 is to the left and 1 is to the right.

#### Functions
1. `__init__(self, s)`
   1. `s` The socket object
   
   Initializes the class with the object s. This will set `up` to the default value and then will instantiate a server object with the socket objected passed into it.
2. `get_data(self)`

   Gets the data from the server for the next move from the client. 
3. `update(self, socket)`

   Updates the position based on the data which was given to it from the client.

### AI_output

This class communicates with the paddleAI class to give and recieve position and trajectory data. The purpose is to encaspulate read and write operations to and from the AI and produce a readable output. 

#### Variables

1. `up`

   This stores information on the movement of the paddle: -1 is to the left and 1 is to the right.

2. `ai`

   This contains a reference to a paddleAI instance.

#### Functions
1. `__init__(self)`

   This initializes the AI_output class. Sets all values to the default and initializes paddleAI() in `ai` variable.
2. `set_input(self, x)`

   An encapsulation of setting up to a value x
3. `get_input(self, new_pos, ball_pos)`
 
   1. `new_pos` The current position of the paddle
   2. `ball_pos` The current position of the ball

   This updates the paddleAI class on important information to calculate its next move
4. `update(self, new_pos, ball_pos)`
   1. `new_pos` current position of paddle
   2. `ball_pos` The current postition of the ball

   This updates the ai on these variables and then tells the AI to calculate its next move based on that information. After that, it updates `up` to tell the paddle what direction it should be moving.

### output

This class contains a container for the output of player one with simulated hardware activity.

#### Variables
1. `MAX_SENSITIVITY`
   
   This is the maximum velocity at which the paddle can move
2. `up`

   This contains information on the movement of the paddle in the x direction
3. `side`

   This contains information on the movement of the paddle in the y direction
4. `data`

   This contains an instance of gyro_data()

#### Functions
1. `__init__(self)`

   This initializes the class and sets all of the variables to their default values
2. `get_data(self)`

   This sets the values of x, y, and z and then calls the gyro_data's set function to store the variables
3. `set_output(self)`

   This sets the output depending on the values of x, y, and z. If x is positive it outputs `MAX_SENSITIVITY`, if negative it outputs -`MAX_SENSITIVITY`. It is the same for each of the directions 
4. `update(self)`

   This just calls `set_output` and `get_data` and is called in the game to update the paddle position.

## Future work

1. Update the variable names so that it is more readable
2. Change the gyro data class and get input from a more realistic simulation of the hardware or hardware itself.
3. Update the LAN output class with changes necessary to get the LAN data working