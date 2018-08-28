#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

p = sense.get_pressure()
t = sense.get_temperature()
h = sense.get_humidity()

t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

message = "Temp: " + str(t) + " Tryck: " + str(p) + " Fuktighet: " + str(h)
  

sense.show_message(message, scroll_speed=0.1)
sense.clear()
