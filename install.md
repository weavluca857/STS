# STS
Save Their Souls is a raspberryPi based project designed to teach students computing topics

Contents of this README
1) Materials
2) Software
3) Additional Resources
4) Setting up the Pi 

          Materials (working list) 

-RaspberryPi 3 Model B
-VILROS RaspberryPi Clear Case    (Recommended) 
-HDMI cable
-HDMI enabled display
-SD card (minimum of 8GB)
-SD card reader                   (only necessary if your computer does not have one) 
-Micro USB (power supply 2.5 amps) 
-USB enabled Mouse
-USB enabled Keyboard 

        Software (working list) 

-SD Memory Card Formatter for Windows
https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/
-New Out Of Box Software (NOOBS) for Pi
downloads.raspberrypi.org/noobs  (copy and past this into your browser for the download) 

        Additional Resources

-https://static.raspberrypi.org/files/legacy/qsg.pdf 
    This is a guide for setting up the Pi. Consider using this if you have any problems with 
the guide written out in this file. 
-https://www.raspberrypi.com/software/
    This source is useful for further instruction on setting up other OS on the Pi and for 
setting up OS for the Pi on mac and linux in addition to Windows. 


        Setting up the Pi (For Windows machines) 

1) Get all of the items on the materials list.
    1.5) mount the Pi to the clear case to prevent damage to the device and make transportation easier.

2) Go to the following link and download the memory card formatter for windows. 
https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/
Wait until the installation is done.

3) Navigate to the folder where the download installed to and run the executable.

4) Plug in your SD card reader and SD card to your computer.

5) double click the "SD Card Formatter" you just downloaded, I leave the shortcut on my desktop for
easy of access. 

6) Find your SD card on the SD Card Formatter Pop-up and Overwrite format the SD card

7) This will take some time to run, during this copy and paste the following into your browser
downloads.raspberrypi.org/noobs
and wait for this download to finish. 

8) When the download has finished, find the zip file and extract all to a location you will access again.
Wait for the SD card to finish formatting. 

9) Once the SD card has finished formatting, go into the extracted NOOB file, copy all of its contents, then 
navigate to the SD card using file explorer, go into it and paste the copied file into the SD card. 
Wait for this process to finish. 

10) Now setup the physical enviornment of the Pi, make sure to connect the Pi to power last! Safely eject the SD card 
from the computer and put it into the Pi (located on the underside of the board under the port labeled DISPLAY). 
Connect the HDMI enabled display to power and connect the HDMI display to the port on the Pi labeled HDMI.  
	*If the Casing to the Pi gets in the way of the HDMI cable, remove the SD card THEN remove the casing and
	continue to use the Pi with no casing while you need the display. When you are done remove the SD card then 
	put on the casing and put your SD card back in to keep everything together and protected. 

11) If all has gone well the display should show a boot process then show a prompt for selecting an OS. 
On this screen select the Raspberry Pi OS Full (32-bit) option then navigate to the network tab and select
the network you would like to connect to for downloading additional packages. Optionally, you can connect
an ethernet instead of connecting to a network for the same effect. 

12) Select install at the top of the prompt with Pi OS Full selected and click yes then wait for the OS to install 
on your device. 

13) Once the OS boots up on your device follow the guided prompts to setup the Pi relevant to your needs. Connect to
a network or keep your ethernet attatched and let the system update itself as necessary. Once the final download
finishes your Pi will be in desktop mode and fully functional to begin operating on. 




