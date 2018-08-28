#!/user/bin/emv python
import RPi.GPIO as GPIO
import time
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Flashing LED
while True:
    GPIO.output(11, True)
    randtime = random.uniform(0.1,0.9)
    time.sleep((randtime))
    GPIO.output(11, False)
    randtime = random.uniform(0.1,0.9)
    time.sleep((randtime))
