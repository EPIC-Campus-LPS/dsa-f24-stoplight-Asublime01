import RPi.GPIO as GPIO #Import Modules
from gpiozero import Button
import time
from signal import pause

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([23,24, 25], GPIO.OUT) #Sets GPIO pins as output
GPIO.setup(26, GPIO.IN)



def stoplight():
    
    while True:
        
        global pin26
        print(pin26)
        
        GPIO.output(23, GPIO.HIGH) #Turns on GPIO pin number 23: Turns on Red
        time.sleep(5) #Pause the program or Num Seconds
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH) #Turns on Green
        time.sleep(4)

        GPIO.output(23, GPIO.HIGH) #Turns on Yellow

        time.sleep(1)
        GPIO.output(24, GPIO.LOW) #Turns off Green
        if pin26 == 0:
            break #Breaks the loop

    
    GPIO.output([23, 24], GPIO.LOW) #Turns off lights
    return
    

while True: #Main loop
    pin26 = GPIO.input(26)
    print(pin26)
    if pin26 == 0: #If button pressed, run script
        stoplight()
    else:
        continue


