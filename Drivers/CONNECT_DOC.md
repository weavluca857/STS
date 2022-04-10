# Connect Docs

## imports
1. board 
   
    Link to docs: https://docs.circuitpython.org/en/latest/shared-bindings/board/index.html
2. digitalio

   Link to docs: https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
3. busio

   Link to docs: https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
4. adafruit_mpu6050
   
   Link to docs: https://docs.circuitpython.org/projects/mpu6050/en/latest/

## Classes

1. gyro

### Variables

1. `i2c` Contains the pointer to the i2c connected module
2. `mpu` Contains the connected gyroscope object connected using i2c.

### Functions

1. `__init__(self)`
   
   This is the initialization function fo the gyro class. It checks to make sure that the device that is running the script has both an i2c and spi interface connected and available. In addition, it checks to make sure that it can communicate with any connected board using the digitalio library.
2. `connect_i2c(self)`

   This connects the board by first instantiating an i2c connection then by instantiating a sensor object which is connected through said i2c object.
3. `return_data(self)`

   This returns the value that is retrieved from the connected sensor. The output is in the form of a tuple (x,y,z) angle data.

## Future work

1. Create a more coherent emulation testing that comes from the gyro class itself and contains simulated data in the format in which the gyro would give the data.
2. Test more reliable on the real hardware once it becomes available.