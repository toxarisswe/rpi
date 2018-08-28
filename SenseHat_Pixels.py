#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

#            X
#    0 1 2 3 4 5 6 7 8
#   0
#   1
#   2
#   3
# Y 4
#   5
#   6
#   7
#   8



g = (0,0,0)
b= (0,255,0)


matrix = [
    g, g, b, g, b, g, g, g,
    g, b, g, g, g, b, g, g,
    b, g, g, g, g, g, b, g,
    b, g, b, b, b, g, b, g,
    g, b, g, b, g, b, g, g,
    g, g, b, b, b, g, g, g,
    g, g, g, b, g, g, g, g,
    g, g, g, b, g, g, g, g
]

sense.set_pixels(matrix)
