#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

sense.show_letter("T", red)
sleep(1)
sense.show_letter("O", blue)
sleep(1)
sense.show_letter("V", green)
sleep(1)
sense.show_letter("E", yellow)
sleep(1)
sense.clear()
