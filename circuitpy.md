# Circuit PI installation process

## Documentation - Lesson  
## Fix up bugs, Finish socket/communication
## CS - Python packages?
## H - S lesson sensor data CE
## User interface - Game - Digital arts and sciences.
## Machine learning and data collection - Opposing
## Human centered computing (UI/Testing)



## Update PI

1. `sudo apt-get update`
2. `sudo apt-get upgrade`
3. `sudo apt-get install python3-pip`
4. `sudo pip3 install --upgrade setuptools`

## Check PI configuration

`cd ~ sudo pip3 install --upgrade adafruit-python-shell wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/ master/raspi-blinka.py sudo python3 raspi-blinka.py`

## Install CircuitPython BME280

`pip3 install adafruit-circuitpython-mpu360`

## install pygame

`pip3 install pygame`

## Run the game

`python3 pong.py`

    This runs a pong game which uses the drivers in the Drivers/ directory
    Currently without hardware attached it is just using simulated data to move the controller.




