#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
r = 255
g = 0
b = 0
red = (255,0,0)
blue = (0,0,255)
while True:
    sense.show_message("Tove", text_colour=red, back_colour=blue, scroll_speed=0.2)

#sense.clear()
