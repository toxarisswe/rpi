#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def gen_colour():    
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

sense.show_letter("X",text_colour=gen_colour(),back_colour=gen_colour())

sleep(2)
sense.clear()
