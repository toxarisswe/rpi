#! /usr/bin/env python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

def rand_x():
    return randint(0,7)

def rand_y():
    return randint(0,7)

def pixel_check(x,y):
    pixel = sense.get_pixel(x,y)
    if pixel == [248, 0, 0]:
        return 1
    elif pixel == [0,0,248]:
        return 1
    else:
        return 0

def clear_matrix(x,y):
    pixels = sense.get_pixels()
    count = 0
    for curr in pixels:
        if curr == [0,0,0]:
            count += 1

    sense.clear()
    message = "Left: " + str(count)
    if count == 0:
        sense.show_message(message,text_colour=[255,255,255])
    elif count < 4:
        print (count)
        sense.show_message(message,text_colour=[0,255,0])
    else:
        sense.show_message(message,text_colour=[255,0,0])
    
    sense.set_pixel(rand_x(),rand_y(),blue)
    sense.set_pixel(rand_x(),rand_y(),blue)
    sense.set_pixel(rand_x(),rand_y(),blue)
    sense.set_pixel(rand_x(),rand_y(),blue)
    sense.set_pixel(x,y,red)

red = (248,0,0)
blue = (0,0,248)

x = rand_x()
y = rand_y()
sense.clear()
    
sense.set_pixel(rand_x(),rand_y(),blue)
sense.set_pixel(rand_x(),rand_y(),blue)
sense.set_pixel(rand_x(),rand_y(),blue)
sense.set_pixel(rand_x(),rand_y(),blue)
sense.set_pixel(x,y,red)

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            
            if event.direction == "up":
                if y == 0: y = 7
                else: y = y-1
                
                if pixel_check(x,y) == 1:
                    x = rand_x()
                    y = rand_y()
                    clear_matrix(x,y)
                else:
                    sense.set_pixel(x,y,red)
                    
            elif event.direction == "down":
                if y == 7: y = 0
                else: y = y+1

                if pixel_check(x,y) == 1:
                    x = rand_x()
                    y = rand_y()
                    clear_matrix(x,y)
                else:
                    sense.set_pixel(x,y,red)
                    
            elif event.direction == "left": 
                if x == 0: x = 7
                else: x = x-1

                if pixel_check(x,y) == 1:
                    x = rand_x()
                    y = rand_y()
                    clear_matrix(x,y)
                else:
                    sense.set_pixel(x,y,red)
                    
            elif event.direction == "right":
                if x == 7: x = 0
                else: x = x+1

                if pixel_check(x,y) == 1:
                    x = rand_x()
                    y = rand_y()
                    clear_matrix(x,y)
                else:
                    sense.set_pixel(x,y,red)
                    
            elif event.direction == "middle":
                x = rand_x()
                y = rand_y()
                clear_matrix(x,y)
