#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
