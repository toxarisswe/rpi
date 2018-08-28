#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.clear(red)
    else:
        sense.clear()
