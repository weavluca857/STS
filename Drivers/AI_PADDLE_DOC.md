# AI Paddle class Docs

The AI class encapsulates getting paddle information from the game into the class where then the update functions will be called. 
The update functions will then call a function which will then determine the next move which the AI wants to take. 

## Imports
NA

## Classes
1. PaddleAI

### Variables:
1. `pos`  contains information about the current position of the paddle
2. `traj` contains information about the AI's decision to move. Currently just the direction
3. `ball_position` contains the current ball position used for calculating next move.

### Functions 
1. `__init__(self)`
This function initializes the AI paddle class. Sets all relevent data to default values. 
2. `update(self, new_position, ball_data)` 

    This function will update both `pos` and `ball_position` in the function variables
   1. `new_position` an integer which contains the updated position of the paddle after game moves the paddle from information about the trajectory given to it.
   2. `ball_data` contains updated information about the ball position when the update function is called.

3. `calc_new_position(self)`

   This function will take the data which it currently possesses (class variables) and will determine how it'd like to move the paddle.
  Currently the AI implemented is a perfect one which will continually follow the ball.
  

## Future steps

In the future, different AI designs will be implemented. 
These future designs will contain:
1. Levels of difficulty of AI
2. Different AI algorithms to achieve those levels of difficulty
3. A more sophisticated computation of the balls trajectory than just its current position