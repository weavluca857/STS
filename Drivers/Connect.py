import board
import digitalio
import busio
# These allow you to access the circuit board from python
import time
import adafruit_mpu6050
# This imports the adafruit api for this specific gyro/accelerometer

# This is created to encapsulate the gyro elements as to be able to create multiple instances of controllers
# if need be
class gyro:
    # When initializing the gyro class, first we make sure that python can connect to the required pins
    # Second we make sure that i2c and spi interfaces are working properly on the device so that we
    # can acquire the necessary data.
    def __init__(self):
        try:
            pin = digitalio.DigitalInOut(board.D4)
        except:
            print("problems with DIO")
        try:
            i2c = busio.I2C(board.SCL, board.SDA) # Check boards i2c
        except:
            print("I2C not working properly")

        try:
            spi = busio.SPI(board.SCLK, board.MOSI, board.MISO) # Check the boards spi
        except:
            print("SPI not working properly")


    def connect_i2c(self):

        self.i2c = board.I2C() # Creates an spi controller which will connect to the board.
        self.mpu = adafruit_mpu6050.MPU6050(self.i2c) # registers the MPU 6050 as the slave device which will
                                                      # communicate with the board to give the revent data.

    def return_data(self):
        return self.mpu.gyro # Returns the gyro data for the board. This will be used in the wrapper classes for data
                              # The wrapper classes will be used to import the data into the game in a reable format.