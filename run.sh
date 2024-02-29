#this script will install packages and run the main program
#this script is intended to run on the raspberry pi for starting up the application

sudo apt-get install python3.6
sudo pip3 install adafruit-circuitpython-fingerprint pyfingerprint tkinter
pip main.py