#from Drivers.Connect import gyro
from random import randrange
from Drivers.AIpaddle import paddleAI
from Drivers.socket_driver import Server

# This is a wrapper class for the gyroscope data. It will contain the data output from the gyroscope and other
# important parameters which will affect the speed and movement of the paddles.
class gyro_data:
    #data = gyro()
    current_traj = [] # contains the current trajectory data.
    MAX_X = 20 # Change on max angle 
    MAX_Y = 20 # Change on max angle
    MAX_Z = 20 # Change on max angle
    def __init__(self):
        self.current_traj = [0,0,0] # Create gyro at the base position


    def set_data(self, x, y, z): # An encapsulation of the current_traj so that we can control the values that
                                # we set.
        self.current_traj = [x, y, z]


class LAN_output:

    up = 0

    def __init__(self, s):
        self.up = 0
        self.server = Server(s)
        self.server.listen()

    def get_data(self):
        self.server.get_data()

    def update(self):
        self.get_data()
        self.up = self.server.data

class AI_output:

    up = 0

    def __init__(self):
        self.up = 0
        self.ai = paddleAI()

    def set_input(self, x):
        self.up = x

    def get_input(self, new_pos, ball_pos):
        self.ai.update(new_pos, ball_pos)

    def update(self, new_pos, ball_pos):
        self.get_input(new_pos, ball_pos)
        self.ai.calc_new_pos()
        self.up = self.ai.traj

# A container class for the output data using the gyroscope data stored in gyro_data.
class output:
    MAX_SENSITIVITY = 1 # the speed of the paddles.
    up = 0 # The angle at which the controller is up. Farther pressed the faster the object moves
    side = 0 # The angle to the side it is. Farther the faster to the side it moves.
    # Initializes the output class to zero movement ( at the top ).
    # Also creates a gyro data class which is a "has a relationship"
    def __init__(self):
        self.up = 0
        self.side = 0
        self.data = gyro_data()

    # Gets data from the gyroscope or test_data
    def get_data(self):
        #Call accelerometer/gyro data or test data
        x = (randrange(3)- 1)/4
        y = 0
        z = 0
        self.data.set_data(x, y, z)
    # Sets the direction and the magnitude of the direction
    def set_output(self):
        # if the data x is negative
        if self.data.current_traj[0] < 0:
            # Round to the nearest min value (-1) * max.
            self.up = int(self.data.current_traj[0]/self.data.MAX_X) - (self.data.current_traj[0] % self.data.MAX_X > 0)
        else:
            # Round to the nearest max value (1) * max
            self.up = int(self.data.current_traj[0] / self.data.MAX_X) + (
                        self.data.current_traj[0] % self.data.MAX_X > 0)\
        # repeat the same sequences with the y values.
        if self.data.current_traj[1] < 0:
            self.side = int(self.data.current_traj[1]/self.data.MAX_Y) - (self.data.current_traj[1] % self.data.MAX_Y > 0)
        else:
            self.side = int(self.data.current_traj[1] / self.data.MAX_Y) + (
                        self.data.current_traj[1] % self.data.MAX_Y > 0)
    # wraps both of the functions in an update function which is called by the game.
    def update(self):
        self.get_data()
        self.set_output()

