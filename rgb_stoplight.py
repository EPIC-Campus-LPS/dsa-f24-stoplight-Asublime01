import RPi.GPIO as GPIO #Import Modules

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup([23,24, 25], GPIO.OUT) #Sets GPIO pins as output
while True:
    GPIO.output(23, GPIO.HIGH) #Turns on GPIO pin number 23: Turns on Red
    time.sleep(5) #Pause the program or Num Seconds
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH) #Turns on Green
    time.sleep(4)
    
    GPIO.output(23, GPIO.HIGH) #Turns on Yellow
    
    time.sleep(1)
    GPIO.output(24, GPIO.LOW) #Turns off Green
    